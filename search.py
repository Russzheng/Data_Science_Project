#!/usr/bin/python

from twitter import *
import csv
import requests

def main():

  config = {}
  execfile("/Users/khsia/Desktop/finalproject/config.py", config)
  twitter = Twitter(
              auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
  runQuery(twitter, "hospital")
  runQuery(twitter, "appointment")
  runQuery(twitter, "hospital appointment")

def runQuery(twitter, word):
  query = twitter.search.tweets(q = word, lang="en", count="100")
  with open("/Users/khsia/Desktop/finalproject/"+word+".csv", 'wb') as outfile:
    writer = csv.writer(outfile)
    for result in query["statuses"]:
      text = result["text"].encode('utf-8')
      payload = {'text': text}
      r = requests.post("http://text-processing.com/api/sentiment/", data=payload)
      positiveValue = r.json()["probability"]["pos"]
      neutralValue = r.json()["probability"]["neutral"]
      negativeValue = r.json()["probability"]["neg"]
      writer.writerow([result["created_at"], text, positiveValue, neutralValue, negativeValue])

if __name__ == '__main__':
    main()
#cronjob
#env EDITOR=nano crontab -e
#00 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py
#15 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py
#30 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py
#45 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py