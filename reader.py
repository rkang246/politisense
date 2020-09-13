import pymongo

class DatabaseHelper:

  def __init__(self):
    self.client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.wcn2l.mongodb.net/PenApps2020?retryWrites=true&w=majority")
    self.db = self.client['PennApps2020']
    self.twitter_sentiment = self.db['twitter_sentiment']
    self.reddit_sentiment = self.db['reddit_sentiment']
    self.cnn_sentiment = self.db['cnn_sentiment']
    self.fox_sentiment = self.db['fox_sentiment']

  def find_by_name(self, name):
    if (name == "Joe Biden"):
      name = "Biden"
    if (name == "Donald Trump"):
      name = "Trump"
    tr = self.twitter_sentiment.find( { "subject": name } )
    for el in tr:
      el.update({'category':'twitter'})
    rr = self.reddit_sentiment.find( { "subject": name } )
    cr = self.cnn_sentiment.find( { "subject": name } )
    for el in cr:
      el.update({'category':'cnn'})
    fr = self.fox_sentiment.find( { "subject": name } )
    for el in fr:
      el.update({'category':'fox'})
    # print(list(tr) + list(rr) + list(cr) + list(fr))
    return list(tr) + list(rr) + list(cr) + list(fr)