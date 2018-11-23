import threading
import time
from news_api import newsApi
"""
from newsapi import NewsApiClient
"""
import requests
from api_mysql2 import nytimes
from twython import Twython
from twitter import twitter
import csv
import json

exitFlag = 0
""""
newsapi = NewsApiClient(api_key='17a51cc53e444a46b84ce26ee223d40d')
"""
APP_KEY = "UKP4lexaxthDyD7JdSoPU6hit"
APP_SECRET = "bgPLO3BINx96qRQoF7r2d8cO2cvYxONJInz2t5lhDrQTRaHExR"
OAUTH_TOKEN = "1022907936287477760-l0Gr2wu8lkEvrg2666wRT1sVpfK4Aq"
OAUTH_TOKEN_SECRET = "Uzh5LhCW0FSEACH3fq93UE7nQDxIApJ2t9VBXSw87S1Zt"



class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      result = run_api(self.threadID)
      print(result)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def run_api(threadID, kwd1, kwd2):
        if threadID == 1:
            tweets = Twython(APP_KEY, APP_SECRET)
            search = tweets.search(q= kwd1, result_type='popular', count=1, include_entities=False)
            result = twitter(search)

            return(result)
        if threadID == 2:
            key = "q="+ kwd1 +"+"+ kwd2 +"&begin_date=20161001&api-key=db6fd2cc8d9c417580e7f19e44f4c8f6"
            r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?", key)
            data = r.json()
            articles = (data["response"]["docs"])
            result = nytimes(articles)

            return(result)
        """
        if threadID == 3:
            top_headlines = newsapi.get_top_headlines(q=kwd1,
                                              sources='bbc-news,the-verge,abc-news,bloomberg,business-insider,business-insider-uk,buzzfeed,cbc-news',
                                              language='en')
            result = newsApi(top_headlines)
            Listener(result)
            return(result)
        """

def Listener(kwd1, kwd2, tkn):
    data = [[kwd1, kwd2, tkn]]

    with open("data_stream.csv", "a") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(data)

    writeFile.close()


# Create new threads
thread1 = myThread(1, "Thread-1", 0)
thread2 = myThread(2, "Thread-2", 0)
thread3 = myThread(3, "Thread-3", 0)


# Start new Threads
thread1.start()
thread2.start()
thread3.start()
