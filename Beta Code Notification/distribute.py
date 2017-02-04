from twython import Twython
import sqlite3 as lite
from betaScraper import Beta
from datetime import datetime, date, time
import data
def main():
    con = lite.connect('beta.db')

    dictionary = []
    APP_KEY = data.APP_KEY
    APP_SECRET = data.APP_SECRET
    ACCESS_TOKEN = data.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = data.ACCESS_TOKEN_SECRET
    twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter.verify_credentials()

    params = {'count': 5}
    home = twitter.get_home_timeline(**params)
    for tw in home:
        dictionary.append(tw['text'])

    # go back a week
    selected_date = datetime.now().date().strftime('%Y%m%d')
    selected_date = int(selected_date) - 7
    with con:
        cur = con.cursor()
        for row in cur.execute('SELECT * FROM beta WHERE start >= ?', (selected_date,)):
            beta = Beta(row[0], row[1], row[2], row[3], row[4])
            if any(beta.title in string for string in dictionary):
                continue
            status = "{0} for {1} ends {2}. Learn more here: {3}".format(beta.event, beta.title, beta.end, beta.url)
            twitter.update_status(status=status)
main()
