import betaScraper
import distribute
import time

while True:
    betaScraper.main()
    distribute.main()
    time.sleep(3600) # sleep for an hour
