import numpy as np
from text_analyser.use_word2vec import load_all_equipment_names
from  text_analyser.use_word2vec import model

def get_similar_words():
    equipments =load_all_equipment_names()
    e_list =[]
    for e in equipments:
        e_list.extend(e)
    e_list = list(set(e_list))

    #for e in e_list:






def restrict_w2v( restricted_word_set):
    w2v = model
    new_vectors = []
    new_vocab = {}
    new_index2entity = []
    new_vectors_norm = []

    for i in range(len(w2v.vocab)):
        word = w2v.index2entity[i]
        vec = w2v.vectors[i]
        vocab = w2v.vocab[word]
        vec_norm = w2v.vectors_norm[i]
        if word in restricted_word_set:
            vocab.index = len(new_index2entity)
            new_index2entity.append(word)
            new_vocab[word] = vocab
            new_vectors.append(vec)
            new_vectors_norm.append(vec_norm)

    w2v.vocab = new_vocab
    w2v.vectors = np.array(new_vectors)
    w2v.index2entity = np.array(new_index2entity)
    w2v.index2word = np.array(new_index2entity)
    w2v.vectors_norm = np.array(new_vectors_norm)