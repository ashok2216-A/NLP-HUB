import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
from nltk import sent_tokenize,word_tokenize
from nltk.stem.snowball import SnowballStemmer


def normalize(text):
    return(text.lower())

def remove_stopwords(text):
  list_stopwords =  stopwords.words("english")
  finalText=' '.join(a for a in word_tokenize(text) if (a not in list_stopwords and a.isalnum()))
  return finalText

def removenumbers(text):
    re_num = "\d+" ###COMPLETE THE REGULAR EXPRESSION
    text = re.sub(re_num, "", text)
    return text

def stem_text(text):
  stemmer = SnowballStemmer("english")
  t=' '.join(stemmer.stem(a) for a in word_tokenize(text))
  return t

def preprocess(text):
  text = normalize(text)
  text = remove_stopwords(text)
  text = removenumbers(text)
  text = stem_text(text)
  return(text)
