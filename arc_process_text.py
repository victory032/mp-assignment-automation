# Import pandas for dataframe 
import pandas as pd 

# Import re, nltk, and WordNetLemmatizer
import re
import nltk
from nltk.stem import WordNetLemmatizer

# Import Tfidf vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('wordnet')

# Import train_rel_2.tsv into Python
with open('data/train_rel_2.tsv', 'r') as f:
    lines = f.readlines()
    columns = lines[0].split('\t')
    response = []
    score = []
    for line in lines[1:]:
        temp = line.split('\t') 
        if temp[1] == '3':   # Select the Essay Set 3
            response.append(temp[-1])  # Select EssayText as response
            score.append(int(temp[2])) # Select score1 for human scoring only
        else: 
            None
            
# Construct a dataframe ("data") which includes response and score column     
data = pd.DataFrame(list(zip(response, score))) 
data.columns = ['response', 'score'] 

# Print how many rows and columns of the data set consists  
print(data.shape)

# Preview the first ten row in the data set
print(data.head(10))  

# Stopword removal, converting uppercase into lower case, and lemmatization
stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
nltk.download('stopwords')
data_without_stopwords = []
for i in range(0, len(response)):
    doc = re.sub('[^a-zA-Z]', ' ', response[i])
    doc = doc.lower()
    doc = doc.split()
    doc = [lemmatizer.lemmatize(word) for word in doc if not word in set(stopwords)]
    doc = ' '.join(doc)
    data_without_stopwords.append(doc)
    
# Print first row in the the original data set 
print(data.response[0]) 

# Print first row in the the data set after preprocessing
print(data_without_stopwords[0])


vectorizer = TfidfVectorizer() 
vectors = vectorizer.fit_transform(data_without_stopwords)

# Print how many rows and columns of the TF-IDF matrix consists
print("n_samples: %d, n_features: %d" % vectors.shape)

# Select the first five documents from the data set
tf_idf = pd.DataFrame(vectors.todense())
# tf_idf = pd.DataFrame(vectors.todense()).iloc[:5]

tf_idf.columns = vectorizer.get_feature_names_out()
tfidf_matrix = tf_idf.T
# tfidf_matrix.columns = ['response'+ str(i) for i in range(1,6)]
tfidf_matrix.columns = ['response'+ str(i) for i in range(len(response))]
tfidf_matrix['count'] = tfidf_matrix.sum(axis=1)

# Top 10 words 
# tfidf_matrix = tfidf_matrix.sort_values(by ='count', ascending=False)[:10] 
tfidf_matrix = tfidf_matrix.sort_values(by ='count', ascending=False) 

# Print the first 10 words 
# print(tfidf_matrix.drop(columns=['count']).head(10))
print(tfidf_matrix[["count"]].head(10))
# print(tfidf_matrix.drop(columns=['count']))

# Output
result_tfidf = tfidf_matrix.index[:10]
print(result_tfidf)