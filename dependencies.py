import warnings
warnings.simplefilter("ignore")
import pandas as pd # data manipulation
from collections import Counter # count word frequency in a string
import re #for regular expression

# data preprocessing
import nltk
# Download the following 3 (three) packages only 1 time during dependency setup
# nltk.download('wordnet')
# nltk.download('stopwords') 
# nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn
from nltk.stem.porter import PorterStemmer #for steming 
from nltk.stem import WordNetLemmatizer #for lemmatization

from nltk.corpus import stopwords 


# similarity check
import spacy
# ! python -m spacy download en_core_web_lg  #Run only 1 time in terminal during dependency setup
