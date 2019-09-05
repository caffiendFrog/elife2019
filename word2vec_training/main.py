#from data_extract.data_download import load_equipment_names, get_all_xml_file_names,preprocess_and_persist_string, process_all_files
from text_analyser.use_word2vec import load_all_equipment_names, get_most_similar, get_distance, compare_noun_phrase_to_equipment_name_list
import spacy

if __name__ == "__main__":
    print(get_distance('mass', 'spectrometer'))

    print(get_distance('argon', 'ion'))
    print(get_distance('microscope', 'microscopy'))
    print(get_distance('microscope', 'microscopes'))
    tokenized_instruments_name = load_all_equipment_names()

    print(compare_noun_phrase_to_equipment_name_list(['organization','fellow'], tokenized_instruments_name))




def something():
    tokenized_instruments_name = load_all_equipment_names()

    for x in tokenized_instruments_name[4 :10]:
        for i in  x:
            print(i)
            print(get_most_similar(i))
            print("")


'''
def main():

    #ngram_data = load_equipment_names()
    #all_xml_file_name = get_all_xml_file_names()
    #process_all_files(all_xml_file_name)

    print(get_most_similar('thermometer'))
    print("")
    print(get_most_similar('bioanalyzer'))
    print("")
    print("")

    print(get_most_similar('cellprofiler'))
    print("")
    print("")

    print(get_most_similar('thermocycler'))
    print("")

    print("")

    print(get_most_similar('centrifugal concentrator'))
    print("")

    print("")

    print(get_most_similar('thermal cycler'))
    print("")




    #for i in range(10):
    #print(preprocess_and_persist_string('/home/michael/pubmed/ACS_Chem_Neurosci/PMC5783156.nxml'))
    #    print("")

    #print(ngram_data)

'''