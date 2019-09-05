from gensim.models import Word2Vec
from os import listdir
import os
from config import PREPROCESSED_ARTICLE_BODY
from data_extract.data_download import  stop_words2
from gensim.models import Phrases

import nltk
from nltk import word_tokenize

def read_all_preprocessed_files ():
    files = listdir(PREPROCESSED_ARTICLE_BODY)
    wordvec_list = []
    for file in files:
        with open( os.path.join(PREPROCESSED_ARTICLE_BODY, file)) as file_reader :
            tokenized_list = nltk.word_tokenize(file_reader.readlines())
            tokenized_list = [word.strip() for word in tokenized_list if word not in stop_words2]
            wordvec_list.append(tokenized_list)
    return wordvec_list

def train_gensim_word2vec(list):
    model = Word2Vec(list, min_count=5)



