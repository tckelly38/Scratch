import praw
import time
import re
import sys
import data
import threading
from threading import Thread
import math

def init():
    bot = praw.Reddit(user_agent=data.user_agent,
                      client_id=data.client_id,
                      client_secret=data.client_secret,
                      username=data.username,
                      password=data.password)
    # matches integers and decimals that end with a '!'
    dec_expression = ' \d+[.,]\d*!'
    expression = ' \d+[!]+'
    neg_expression = '-\d+[.,]?\d*!'
    return bot, expression, neg_expression, dec_expression

def mult_factorial(num, num_exclam):
    result = 1
    for i in range(num, 0, -1 * num_exclam):
        result = result * i
    return result

def work(text, author, subreddit):
    if re.search(neg_expression, text) is None and \
       (re.search(expression, text) is not None or \
       re.search(dec_expression, text) is not None) and \
       author is not data.avoid_authors:
       print text
       number = re.search(expression, text)
       if number is None or number is '':
           return
       # remove all '!' from number
       num = number.group(0).replace('!', '')
       num = num[1:]
       if num is None or num == '' or num == '1' or num == '2':
           return
       if re.search(dec_expression, text) is not None:
           if float(num) > 171.0:
               return
           result = math.gamma(int(num) + 1)
       else:
           num_exclam = number.group(0).count('!')
           if num_exclam > 1:
               result = mult_factorial(int(num), num_exclam)
           else:
               result = math.factorial(int(num))
       message = "So when you say `{0}`,  do you mean {1}?".format(number.group(0)[1:], result)
       #check message fits
       if len(message) > 10000:
           return
       print "\n\nAuthor: {0}\nSubreddit: {1}\nLink: {2}\nDate/Time: {3}\n\n".format(author, subreddit, message, time.strftime("%c"))
       return message

def Comments(bot, expression, neg_expression, dec_expression):
    for comment in bot.subreddit('all').stream.comments():
        message = work(comment.body, comment.author, comment.subreddit)
        if message is not None:
            comment.reply(message)

def Submissions(bot, expression, neg_expression, dec_expression):
    for submission in bot.subreddit('all').stream.submissions():
        message = work(submission.title, submission.author, submission.subreddit)
        if message is not None:
            submission.reply(message)

if __name__ == "__main__":
    bot, expression, neg_expression, dec_expression = init()
    comment_thread = Thread(target = Comments, args=(bot, expression, neg_expression, dec_expression))
    submission_thread = Thread(target = Submissions, args=(bot, expression, neg_expression, dec_expression))
    comment_thread.start()
    comment_thread.join()
    submission_thread.start()
    submission_thread.join()
