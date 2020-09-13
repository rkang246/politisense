# LAUNCH THIS SITE FOR EVERYTHING!
#$ export FLASK_APP=launch_site.py
#$ export FLASK_APP=launch_site.py
#go to localhost
from flask import Flask, render_template, url_for, redirect, request
from reader import DatabaseHelper
from functools import reduce

app = Flask(__name__)
helper = DatabaseHelper()

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        data = str(request.form["search"])
        print("Search query: ", data)
        values = getPoliticalSentiment(data)
        #TODO: change jinja templating after search goes through or reroute to new template

        return render_template("index.html", query_made=True, previous_query=data)

    elif (request.method == 'GET'):
        return render_template("index.html", query_made=False, previous_query="")


def getPoliticalSentiment(name):
  sentimentScores = helper.find_by_name(name)
  sentimentScores = [score['sentiment'] for score in sentimentScores]
  averageSentiment = reduce(lambda x, y: x + y, sentimentScores) / len(sentimentScores)
  print(averageSentiment)
  return averageSentiment