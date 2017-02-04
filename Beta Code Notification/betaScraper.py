import urllib2
from BeautifulSoup import BeautifulSoup
import re
import sqlite3 as lite
from datetime import datetime, date, time
class Beta:
    def __init__(self, title, event='', start='', end='', url=''):
        self.title = title
        self.event = event
        self.start = start
        self.end = end
        self.url = url
def main():
    con = lite.connect('beta.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Beta (title TEXT PRIMARY KEY UNIQUE, event TEXT, start TEXT, end TEXT, url TEXT );")

    content = 'http://games.gamepressure.com/beta-tests.asp'
    col_data = []
    row_data = []
    beta_a = []
    soup = BeautifulSoup(urllib2.urlopen(content).read())
    table = soup.find('table', attrs={'class': 'table13 table13-1'})
    table_body = table.find('tbody')
    rows = table_body.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        for col in cols:
            col = [ele.text.strip() for ele in col]
            col_data.append([ele for ele in col if ele])
        row_data.append(col_data)
        col_data = []
    for row in row_data:
        #convert date from 03 February 2017 to 20170203 for easy comparison in sqlite3
        dt = datetime.strptime(re.search(r'\d{2} [a-zA-Z]* \d{4}',  row[2][2]).group(0), '%d %B %Y').date()
        dt = dt.strftime('%Y%m%d')

        beta = Beta(row[1][0], \
                    row[2][0], \
                    dt, \
                    row[2][3][3:], \
                    re.search("(?P<url>https?://[^\s]+)", row[3][0]).group("url"))
        beta_a.append(beta)
        beta = None

    for b in beta_a:
        with con:
            cur = con.cursor()
            cur.execute("INSERT OR IGNORE INTO Beta(title, event, start, end, url) VALUES (?, ?, ?, ?, ?);", \
                        (b.title, b.event, b.start, b.end, b.url))
    print "done"
main()
