import nltk #Natural Language Toolkit, It provides tools to process and analyze human language.
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer #It is used to reduce words to their root or stem form.
from nltk.tokenize import word_tokenize

nltk.download('punkt') #Purpose:Tokenization
nltk.download('punkt_tab') #Additional tokenizer data
nltk.download('stopwords') #Common English words

text = """ Natural Language Processing is a field of Artificial Intelligence.It helps computers understand and process human language."""

print("Original Text:")
print(text)

words = word_tokenize(text) #Splits the input text into individual words and punctuation marks.

words = [word.lower() for word in words]

words = [word for word in words if word.isalnum()] #Removes punctuation and special characters., isalnum() checks whether a string contains only letters or numbers.

stop_words = set(stopwords.words('english')) #Loads the English stopwords list.,set() stores words in a set for efficient membership checking.
filtered_words = [word for word in words if word not in stop_words]

print("\nAfter Stop Word Removal:")
print(filtered_words)

stemmer = PorterStemmer() #Creates an object of the PorterStemmer class.
stemmed_words = [stemmer.stem(word) for word in filtered_words] #Applies stemming to every word in filtered_words

print("\nAfter Stemming:")
print(stemmed_words)
