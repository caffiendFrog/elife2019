from config import EQUIPMENT_FILE_NAME


import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import everygrams
from nltk.corpus import stopwords


from glob import glob




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
            all_ngram = list(set(all_ngram + tokenize_lemmatize(line)))
        return all_ngram


def tokenize_lemmatize(sentence) :
    sentence = sentence.lower().strip('"')
    lemmatizer = WordNetLemmatizer()
    tokenized_list = nltk.word_tokenize(sentence)
    tokenized_list = [word for word in tokenized_list if word not in stop_words]

    lemmatized_word_list = [lemmatizer.lemmatize(w) for w in tokenized_list]
    every_gramm_list = list(everygrams(lemmatized_word_list, 2, 4))
    #print(every_gramm_list)
    return [' '.join(gram) for gram in every_gramm_list]


def get_all_xml_files():
    files = []
    start_dir = os.getcwd()
    pattern = "*."

    for dir, _, _ in os.walk(start_dir):
        files.extend(glob(os.path.join(dir, pattern)))
    return None






