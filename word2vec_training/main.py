#from data_extract.data_download import load_equipment_names, get_all_xml_file_names,preprocess_and_persist_string, process_all_files
from text_analyser.use_word2vec import load_all_equipment_names, get_most_similar, get_distance, compare_noun_phrase_to_equipment_name_list, get_all_noun_phrases, get_phrase_in_text

PMC5080681= 'In this study, the following instruments were used: Gas Chromatography Mass Spectrometry (GC-MS) (QP-5000 GC-MS Shimadzu, Japan), ultrasonic-microwave cooperative extractor/reactor (CW-2000, China), rotary evaporator (Heidolph OB2000, VV2000, Germany), UV visible spectrophotometer (Jenway 7315, England), grinder (Moulinex model, Uno. China), balance (Radw ag, AS 220/c/2, Poland), filter paper (Machrery-Nagel, MN 617 and Whatman no.1, USA), micropipettes (Finnpipette, Finland), incubator (Nuve, Turkey), syringe filter 0.45 μm pore size (Microlab, China) and 96-well plates (Greiner bio-one, North America).'
PMC6602964_1 = 'The method described by Ramar et al. 69 was followed for adulticidal bioassay against Aedes aegypti, where acetone was used as a solvent. Initially, 100 and 1000 ppm concentration of each EO were tested against adult Aedes aegypti. 2 ml of each prepared solution was applied on Whatman no. 1 filter papers (size 12 × 15 cm 2) and allowed to evaporate acetone for 10 minutes. Filter paper treated with 2 ml of acetone alone was used as control. After evaporation of acetone, both the treated and the control filter paper were placed in cylindrical tubes (depth 10 cm). Ten numbers of 3–4 days old non-blood fed mosquitoes were transferred in each of the three replicas of each concentration. Based on the result of initial test, different concentrations of the selected oils were tested. Mortality was recorded at 1 hour, 2 hour, 3 hour, 4 hour, 5 hour, 6 hour, 24 hour, 48 hour and 72 hour respectively from the time of the mosquito released. LC50 value was calculated at 24 h, 48 h and 72 h of exposure period. If mortality exceeded 20% in the control batch, the whole test was repeated. Again, if mortality in the controls was above 5%, results with the treated samples were corrected using Abbott’s formula 68.'
PMC6602964_2 ='For analysis of the constituent compounds of the selected EO, Gas chromatography (Agilent 7890A) and mass spectrometry (Accu TOF GCv, Jeol) was performed. GC was equipped with a FID detector and a capillary column (HP5- MS). The carrier gas was helium at a flow rate of 1 ml/min. The GC programme was set for Allium sativum as 10: 80- 1M- 8-220-5M-8-270-9M, for Ocimum sanctum as 10:80-3M-8-200-3M-10-275-1M-5-280, for Mentha piperita as 10:80-1M-8-200-5M-8-275-1M-5-280, for Eucalyptus maculata as 20,60-1M-10-200-3M-30-280, and for Callistemon linearis as 10: 60-1M-8-220-5M-8-270-3M respectively.'



if __name__ == "__main__":
    #print(get_distance('mass', 'spectrometer'))
    #print(get_distance('argon', 'ion'))
    #print(get_distance('microscope', 'microscopy'))
    #print(get_distance('microscope', 'microscopes'))
    tokenized_instruments_name = load_all_equipment_names()
    #print(get_all_noun_phrases(test_text))
    print(get_phrase_in_text(PMC5080681, tokenized_instruments_name))
    print("")
    print(get_phrase_in_text(PMC6602964_1, tokenized_instruments_name))
    print("")
    print(get_phrase_in_text(PMC6602964_2, tokenized_instruments_name))
    #compare_noun_phrase_to_equipment_name_list()

    #print(compare_noun_phrase_to_equipment_name_list(['organization','fellow'], tokenized_instruments_name))


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