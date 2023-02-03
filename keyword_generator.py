# Import re, nltk, and WordNetLemmatizer
import re
import nltk
from nltk.stem import WordNetLemmatizer

from collections import Counter

nltk.download('stopwords')
nltk.download('wordnet')

def read_pdf():
  return "China's panda and Australia's koala are two animals that arent predator, pandas eat bamboo and koala's eat eucalyptus leaves. Therefore, they are harmless. They are both different from pythons because pythons are potentialy dangerous considering they can swallow an entire alligator you could conceivably have pythons shacking upto the Potomac"

def preprocess_text(text):
    # Stopword removal, converting uppercase into lower case, and lemmatization
    stopwords = nltk.corpus.stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    
    p_text = re.sub('[^a-zA-Z]', ' ', text)
    p_text = p_text.lower()
    p_text = p_text.split()
    p_text = [lemmatizer.lemmatize(word) for word in p_text if not word in set(stopwords)]
    p_text = ' '.join(p_text)
    
    return p_text

def get_keywords():
  text = read_pdf() 
  text = preprocess_text(text)
  term_frequencies = Counter(text.split())
  potential_words = term_frequencies.most_common()[:5]

  keywords = []
  for word, _ in potential_words:
    keywords.append(word)
  # print(keywords)
  return keywords