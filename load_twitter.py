import json
import bz2
import nltk
import os
import pymongo

# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk('./twitter_data'):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
print(listOfFiles)

client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.wcn2l.mongodb.net/PenApps2020?retryWrites=true&w=majority")
db = client['PennApps2020']
tweet_sentiment = db['tweet_sentiment']

politicians = ['Biden', 'Trump', 'Kamala Harris', 'Mike Pence']
for file in listOfFiles: 
  tweets = []
  try:
    with bz2.open(file) as json_file:
      lines = json_file.readlines() 
      for line in lines:
        data = json.loads(line)
        try:
          if (any(ele in data['text'] for ele in politicians)):
            processed = {}
            processed['text'] = data['text']
            processed['retweet_count'] = data['retweet_count']
            processed['favorite_count'] = data['favorite_count']
            processed['sentiment'] = sid.polarity_scores(data['text'])['compound']
            def filterpoliticians(name):
              if name in data['text']:
                return name
            processed['subject'] = list(filter(lambda a: a in data['text'], politicians))
            
            tweets.append(processed)
        except:
          print("Error: current line not readable")

  except:
    print(f'Couldnt read file {file}')

  print(f'Finished processing {file}...')
  if tweets != []:
    tweet_sentiment.insert_many(tweets)
