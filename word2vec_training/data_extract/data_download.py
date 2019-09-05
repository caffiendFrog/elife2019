from config import EQUIPMENT_FILE_NAME, TRAINING_DATA_DIR


import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import everygrams
from nltk.corpus import stopwords
import os

from glob import glob

import xml.etree.ElementTree as ET

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

stop_words = stopwords.words('english')
stop_words.append("'")
stop_words.append("''")
stop_words.append(".")
stop_words.append(")")
stop_words.append("(")
stop_words.append("&")

stop_words.append("system")
stop_words.append("analyzer")
stop_words.append("function")
stop_words.append('documentation')
#stop_words.append("science")
#stop_words.append("scientific")


def load_equipment_names () :
    with open(EQUIPMENT_FILE_NAME) as equipment_files:
        all_ngram = list()
        for line in equipment_files:
            all_ngram = list(set(all_ngram + tokenize_lemmatize_ngram(line)))
        return all_ngram


def tokenize_lemmatize_ngram(sentence) :
    sentence = sentence.lower().strip('"')
    lemmatizer = WordNetLemmatizer()
    tokenized_list = nltk.word_tokenize(sentence)
    tokenized_list = [word for word in tokenized_list if word not in stop_words]

    lemmatized_word_list = [lemmatizer.lemmatize(w) for w in tokenized_list]
    every_gramm_list = list(everygrams(lemmatized_word_list, 2, 4))
    #print(every_gramm_list)
    return [' '.join(gram) for gram in every_gramm_list]

def tokenize_lemmatize(sentence) :
    sentence = sentence.lower().strip('"')
    lemmatizer = WordNetLemmatizer()
    tokenized_list = nltk.word_tokenize(sentence)
    tokenized_list = [word.strip() for word in tokenized_list if word not in stop_words]

    lemmatized_word_list = [lemmatizer.lemmatize(w) for w in tokenized_list]
    return ' '.join(lemmatized_word_list)


def get_all_xml_file_names():
    files = []
    pattern = "*.nxml"

    for dir, _, _ in os.walk(TRAINING_DATA_DIR):
        files.extend(glob(os.path.join(dir, pattern)))

    print(files[0:3], len(files))
    return files

def preprocess_and_persist_string(file_name):
    file_content = get_xml_file_content(file_name)
    return tokenize_lemmatize(file_content)


def get_xml_file_content(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    elements = ['. '.join(elem.itertext()) for elem in root.iter() if elem.tag == 'body']
    return '. '.join(elements)








