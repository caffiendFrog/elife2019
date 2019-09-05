from gensim.models import KeyedVectors
from config import WORD2VEC_MODEL_LOCATION, EQUIPMENT_FILE_NAME, SINGLE_WORD_DISTANCE_THRESHOLD, SINGLE_PHRASE_DISTANCE_THRESHOLD
import spacy
from nltk.corpus import stopwords


model =  KeyedVectors.load_word2vec_format(WORD2VEC_MODEL_LOCATION, binary=True)
nlp = spacy.load("en")
stop_words = stopwords.words('english')
stop_words.extend(["'"'', "''", ".",")", "(", "&","\n", '', '_', '\\', '/', '-'])

def get_most_similar(word, number_of_terms=1):
    try:
        return model.most_similar(word, topn=70)
    except:
        return

def get_distance(word1, word2 ):
    return model.distance(word1, word2)


def load_all_equipment_names():
    tokenized_equimpment = []
    for file in EQUIPMENT_FILE_NAME :
        with open(file) as equipment_files:
            for line in equipment_files:
                sentence = nlp(line)
                tokenized_list = [word.text.strip().lower() for word in sentence if word.text.strip().lower() not in stop_words]
                tokenized_equimpment.append(tokenized_list)
    return tokenized_equimpment


def get_phrase_in_text(document_text, all_equipments):
    noun_phrase_list = get_all_noun_phrases(document_text)
    noun_phrase_suggestion = []
    for noun_phrase in noun_phrase_list:
        sentence = nlp(noun_phrase)
        noun_phrase_split = [word.text.strip().lower() for word in sentence if word.text.strip().lower() not in stop_words]

        if compare_noun_phrase_to_equipment_name_list(noun_phrase_split, all_equipments):
            noun_phrase_suggestion.append(noun_phrase)

    return noun_phrase_list


def get_all_noun_phrases(document_text):
    doc = nlp(document_text)
    try:
        noun_phrases = []
        for np in doc.noun_chunks:
            noun_phrases.append(np.text)
        return noun_phrases
    except:
        return document_text


def compare_noun_phrase_to_equipment_name_list(word_list, all_equipments,):
    for equipment in all_equipments:
        distance_list = []
        for word in equipment :
            for new_word in word_list:
                try:
                    dist =get_distance(word, new_word)
                    if dist < SINGLE_WORD_DISTANCE_THRESHOLD:
                        distance_list.append(dist)
                        continue
                except:
                    continue
        if len(distance_list)> 0 and sum(distance_list)/len(distance_list) < SINGLE_PHRASE_DISTANCE_THRESHOLD:
            return True
    return  False