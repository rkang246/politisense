import pymongo

class DatabaseHelper:

  def __init__(self):
    self.client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.wcn2l.mongodb.net/PenApps2020?retryWrites=true&w=majority")
    self.db = self.client['PennApps2020']
    self.twitter_sentiment = self.db['twitter_sentiment']
    self.reddit_sentiment = self.db['reddit_sentiment']

  def find_by_name(self, name):
    if (name == "Joseph Biden"):
      name = "Biden"
    if (name == "Donald Trump"):
      name = "Trump"
    tr = self.twitter_sentiment.find( { "subject": name } )
    rr = self.reddit_sentiment.find( { "subject": name } )
    return list(tr) + list(rr)