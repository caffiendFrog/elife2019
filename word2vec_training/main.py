from data_extract.data_download import load_equipment_names, get_all_xml_file_names,preprocess_and_persist_string, process_all_files
from train_word2vec.train import


if __name__ == "__main__":

    ngram_data = load_equipment_names()
    all_xml_file_name = get_all_xml_file_names()
    process_all_files(all_xml_file_name)




    #for i in range(10):
    #print(preprocess_and_persist_string('/home/michael/pubmed/ACS_Chem_Neurosci/PMC5783156.nxml'))
    #    print("")

    #print(ngram_data)

