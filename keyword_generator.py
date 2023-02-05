# Import re, nltk, and WordNetLemmatizer
import re
import nltk
from nltk.stem import WordNetLemmatizer

from collections import Counter

import read_pdf_pypdf as r

# nltk.download('stopwords')
# nltk.download('wordnet')

def preprocess_text(text):
	"""This function will do a preprocessing of the text input

	Args:
			str: text input to preprocess (unpreprocessed text)

	Returns:
			str: preprocessed text
	"""
	stopwords = nltk.corpus.stopwords.words('english')
	lemmatizer = WordNetLemmatizer()
	
	p_text = re.sub('[^a-zA-Z]', ' ', text)
	p_text = p_text.lower()
	p_text = p_text.split()
	p_text = [lemmatizer.lemmatize(word) for word in p_text if not word in set(stopwords)]
	p_text = ' '.join(p_text)
    
	return p_text

def get_keywords(text):
  """This function will be used to get the keywords from the preprocessed text

  Args:
      text (str): preprocessed text

  Returns:
      list: top 5 keywords from the text input
  """
  text = preprocess_text(text)
  term_frequencies = Counter(text.split())
  potential_words = term_frequencies.most_common()[:5]

  keywords = []
  for word, _ in potential_words:
    keywords.append(word)
  # print(keywords)
  return keywords