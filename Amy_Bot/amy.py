import praw
import time
import re
import sqlite3 as lite
import sys
import data

bot = praw.Reddit(user_agent=data.user_agent,
                client_id=data.client_id,
                client_secret=data.client_secret,
                username=data.username,
                password=data.password)

amazon_expression = 'http[s]://www.amazon.com/.*/dp[^).\n ]*'
bad_amazon_expression = '\]\(http[s]://www.amazon.com/.*'
subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()
banned_subs = ['audiophile', 'IAmA', 'MechanicalKeyboards', 'CCW', 'SuggestALaptop']

for comment in comments:
    text = comment.body
    author = comment.author
    title = comment.submission.title
    if 'amazon' in text:
        print text
    if re.search(bad_amazon_expression, text) is None and \
       re.search(amazon_expression, text) is not None and \
       author is not data.avoid_authors:# and \
      # comment.subreddit is not in banned_subs:
        print text
        link = re.search(amazon_expression, text)
        if link is None:
            continue
        dp = re.search('http[s]://www.amazon.com/.*/dp/(.*)/[^).\n ]*', link.group(0))
        if dp is None:
            continue
        message = "For less messy amazon links you can extract the part after \"/dp/\" in \n\n {0}\n\nand make it:\n\nhttps://amzn.com/{1}\n\n Or via [smile](http://smile.amazon.com/gp/chpf/about/ref=smi_aas_redirect?ie=UTF8&*Version*=1&*entries*=0) link:\n\n https://smile.amazon.com/dp/{2}\n\n----\n\n**BEEP BOP**\n\nPlz send any recommendations via PM".format(link.group(0), dp.group(1), dp.group(1))
        comment.reply(message)
        print "\n\nAuthor: {0}\nPost: {1}\nSubreddit: {2}\nLink: {3}\nDate/Time: {4}\n\n".format(author, title, comment.subreddit, dp.group(1), time.strftime("%c"))
