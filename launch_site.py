# LAUNCH THIS SITE FOR EVERYTHING!
#$ export FLASK_APP=launch_site.py
#$ export FLASK_APP=launch_site.py
#go to localhost
from flask import Flask, render_template, url_for, redirect, request
from reader import DatabaseHelper
from functools import reduce
import random

app = Flask(__name__)
helper = DatabaseHelper()

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        data = str(request.form["search"])
        print("Search query: ", data)
        query_result = getPoliticalSentiment(data)
        #TODO: change jinja templating after search goes through or reroute to new template

        return render_template("index.html", query_made=True, previous_query=data, query_sentiment=query_result['sentiment'], query_example=query_result['example'], query_percent = round(query_result['sentiment'] * 100,3) )

    elif (request.method == 'GET'):
        return render_template("index.html", query_made=False, previous_query="")


def getPoliticalSentiment(name):
  sentimentBlobs = helper.find_by_name(name)
  random.shuffle(sentimentBlobs)
  sentimentScores = [score['sentiment'] for score in sentimentBlobs]
  averageSentiment = reduce(lambda x, y: x + y, sentimentScores) / len(sentimentScores)
  example = "Mike Pence seen with local firefighters"
  for blob in sentimentBlobs:
    if abs(blob['sentiment'] - averageSentiment) < 0.1:
      example = blob['text']
      break
  result = {}
  result['sentiment'] = averageSentiment
  result['example'] = example
  print(result)
  return result