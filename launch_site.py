# LAUNCH THIS SITE FOR EVERYTHING!
#$ export FLASK_APP=launch_site.py
#$ flask run
#go to localhost
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        data = str(request.form["search"])
        print("Search query: ", data)
        # TODO: make sure request isn't empty
        #TODO: run aveek's functions here?
        #       input: python string (a search term)
        #TODO: change jinja templating after search goes through or reroute to new template

        return render_template("index.html", query_made=True, previous_query=data)

    elif (request.method == 'GET'):
        return render_template("index.html", query_made=False, previous_query="")