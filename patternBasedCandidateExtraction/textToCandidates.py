# -*- coding: utf-8 -*-
"""
Please enter the folder containig the papers as first argument. 
The program will look in each folder that is named "PMC*" for a file named scholarly.html, that contains the text.
The corpus used for development is available under https://github.com/petermr/CEVOpen
Please modify line 21 and 23 to use other file names.
"""
import re
import os
import sys

try:
    home=sys.argv[1]
    filenames = os.listdir(home)
except IndexError:
    home="C:/Users/Sabine/CEVOpen/oil1000/"
    filenames= os.listdir (home)
    

candidatesList=[]
for filename in filenames:
    if "PMC" in filename:
        try:
            with open(home+filename+"/scholarly.html", encoding="utf8") as f:
                #match1 = re.compile(r'using a ((\w+ ){3})')
                #match2= re.compile(r'with a ((\w+ ){3})')
                #" with a " " in a "
                magicList=[" using a ","were used: ", "We used ", " using ",
                           " performed by ", "carried out by ", " via ", " equipped with a ",
                           "maintained on ", " fitted with a ", "was done using a "]
                matchList=[]
                #candidatesList=[]
                for it in magicList:
                    match= re.compile(re.escape(it)+ r'((\w+ ){3})')
                    matchList.append(match)
                    match2=re.compile(re.escape(it)+ r'((\w+ ){4})')
                    matchList.append(match2)
                    #match3=re.compile(r'HP [+\d]')
                    #matchList.append(match3)
                    #match4= re.compile(r'HP-+\d')
                    #matchList.append(match4)
                for line in f:
                    if any(word in line for word in magicList):
                        for match in matchList:
                            candidates=match.findall(line)
                            if len(candidates)>0:
                                candidatesList.extend(candidates)
                # if you want to print the output to a file, do it here
                print(filename)
                for candidate in candidatesList:
                    print(candidate[0])
        except FileNotFoundError:
            continue
        
#to print out all the candidates fond, uncomment this bit
"""
for candidate in candidatesList:
    print(candidate[0])
print(len(candidatesList))
"""