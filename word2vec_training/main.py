from data_extract.data_download import load_equipment_names, tokenize_lemmatize
import os

FILE_NAME = "alaska-equipments"

if __name__ == "__main__":

    ngram_data = load_equipment_names()
    print(ngram_data)

