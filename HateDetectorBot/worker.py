import praw
import data
import threading
from threading import Thread
import time
def init():
    bot = praw.Reddit(user_agent=data.user_agent,
                      client_id=data.client_id,
                      client_secret=data.client_secret,
                      username=data.username,
                      password=data.password)

    return bot


def work(author):
    offending_comments = []
    offending_submissions = []
    user_comment_thread = Thread(target = AnalyzeComments, args=(author, offending_comments))
    user_submission_thread = Thread(target = AnalyzeSubmissions, args=(author, offending_submissions))
    user_comment_thread.start()
    user_submission_thread.start()
    user_comment_thread.join()
    user_submission_thread.join()

    if len(offending_comments) < 1 and len(offending_submissions) < 1:
        return
    message = "This user, /u/{0}, frequently posts in [known hate](https://www.reddit.com/r/AgainstHateSubreddits/comments/68damg/list_of_hate_subreddits/) subreddits.\n\nHere are some of the offending posts:\n\n".format(author)
    if len(offending_comments) > 1 and len(offending_submissions) > 0:
        item_count = 1
        for submission in offending_submissions:
            if item_count < 4:
                message += "{0}) [{1}]({2})\n\n".format(item_count, submission.title, submission.shortlink)
                item_count += 1
            if item_count >= 4:
                break
        if item_count >= 4:
            return message
        for comment in offending_comments:
            if item_count < 4:
                message += "{0}) [{1}](https://www.reddit.com{2})\n\n".format(item_count, comment.body, comment.permalink())
                item_count += 1
            if item_count >= 4:
                break
        return message
    if len(offending_submissions) > 2:
        item_count = 1
        for submission in offending_submissions:
            if item_count < 4:
                message += "{0}) [{1}]({2})\n\n".format(item_count, submission.title, submission.shortlink)
                item_count += 1
            if item_count >= 4:
                break
        return message
    if len(offending_comments) > 2:
        item_count = 1
        for comment in offending_comments:
            if item_count < 4:
                message += "{0}) [{1}](https://www.reddit.com{2})\n\n".format(item_count, comment.body, comment.permalink())
                item_count += 1
            if item_count >= 4:
                break
        return message
    return

def AnalyzeSubmissions(author, offending_submissions):
    for submission in author.submissions.new(limit=25):
        if submission.subreddit in data.hate_subs:
            offending_submissions.append(submission)

def AnalyzeComments(author, offending_comments):
    for comment in author.comments.new(limit=25):
        if comment.subreddit in data.hate_subs:
            offending_comments.append(comment)

def Comments(bot):
    for comment in bot.subreddit('AskReddit').stream.comments():
        if comment.subreddit not in data.hate_subs:
            message = work(comment.author)
            if message is not None:
                print comment.author, comment.subreddit, comment.body
                try:
                    comment.reply(message)
                except Exception as error:
                    print "need to sleep for {0}\n".format(60*9)
                    time.sleep(60*9)
                    print "waking up\n"


def Submissions(bot):
    for submission in bot.subreddit('all').stream.submissions():
        message = work(submission.author)
        if message is not None:
            submission.reply(message)
if __name__ == "__main__":
    bot = init()
    Comments(bot)
    # comment_thread = Thread(target = Comments, args=(bot))
    # submission_thread = Thread(target = Submissions, args=(bot))
    # comment_thread.start()
    # comment_thread.join()
    # submission_thread.start()
    # submission_thread.join()
