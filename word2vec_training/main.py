from data_extract.data_download import load_equipment_names, get_all_xml_file_names,preprocess_and_persist_string
import os

FILE_NAME = "alaska-equipments"

if __name__ == "__main__":

    ngram_data = load_equipment_names()
    all_xml_file_name = get_all_xml_file_names()
    #for i in range(10):
    print(preprocess_and_persist_string('/home/michael/pubmed/ACS_Chem_Neurosci/PMC5783156.nxml'))
    #    print("")

    #print(ngram_data)

