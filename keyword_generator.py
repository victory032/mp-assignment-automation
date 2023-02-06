# Import re, nltk, and WordNetLemmatizer
import re
import nltk
from nltk.stem import WordNetLemmatizer
from collections import Counter

import load_env as e
import openai
openai.api_key = e.OPENAI_API_KEY

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
    p_text = [lemmatizer.lemmatize(word)
              for word in p_text if not word in set(stopwords)]
    p_text = ' '.join(p_text)

    return p_text


def get_keywords(text, api=False):
    """This function will be used to get the keywords from the preprocessed text

    Args:
        text (str): preprocessed text
        api (bool, optional): If the parameter is set to True, it will generate keywords with api api. Defaults to False.

    Returns:
        list: top 5 keywords from the text input
    """

    if api:
        prompt = "Find the most useful terms in this text below. Only print out the terms. \n\n" + text

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )

        keywords = response['choices'][0]['text']

    else:
        text = preprocess_text(text)
        term_frequencies = Counter(text.split())
        potential_words = term_frequencies.most_common()[:5]

        keywords = []
        for word, _ in potential_words:
            keywords.append(word)
        # print(keywords)

    return str(keywords)
