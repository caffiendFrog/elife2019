from config import EQUIPMENT_FILE_NAME


import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import everygrams

nltk.download('wordnet')
nltk.download('punkt')


def load_equipment_names () :
    with open(EQUIPMENT_FILE_NAME) as equipment_files:
        all_ngram = list()
        for line in equipment_files:
            all_ngram = list(set(all_ngram + tokenize_lemmatize(line)))
        return  all_ngram


def tokenize_lemmatize(sentence) :
    lemmatizer = WordNetLemmatizer()
    tokenized_list = nltk.word_tokenize(sentence)
    lemmatized_word_list = [lemmatizer.lemmatize(w) for w in tokenized_list]
    every_gramm_list = list(everygrams(lemmatized_word_list, 1, 3))
    return [' '.join(gram) for gram in every_gramm_list]








