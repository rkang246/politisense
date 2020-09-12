import pandas as pd
import numpy as np
import seaborn as sns
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import calendar
import datetime
import statistics

all_df = pd.read_pickle('all-results.pkl')
sorted_all_df = all_df.sort_values('created_utc', ascending=True)