#Uses the Twitter API to obtain tweets related to hospital, appointment, and hospital appointment
#Config file not uploaded to github due to sensitive and personal information (e.g. login information)

from twitter import *
import csv
import requests
import os

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
  with open("/Users/khsia/Desktop/finalproject/" + word+".csv", 'a') as outfile:
    writer = csv.writer(outfile)
    for result in query["statuses"]:
      text = result["text"].encode('utf-8')
      payload = {'text': text}
      r = requests.post("http://text-processing.com/api/sentiment/", data=payload)
      positiveValue = round(r.json()["probability"]["pos"], 2)
      neutralValue = round(r.json()["probability"]["neutral"], 2)
      negativeValue = round(r.json()["probability"]["neg"], 2)
      writer.writerow([result["created_at"], text, positiveValue, neutralValue, negativeValue])

if __name__ == '__main__':
    main()
#cronjob
#env EDITOR=nano crontab -e
#00 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py
#15 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py
#30 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py
#45 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python /Users/khsia/Desktop/finalproject/search.py