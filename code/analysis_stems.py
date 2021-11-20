#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
path.join("utils/")
from utils.DataUnifier import DataUnifier
from os import listdir
from nltk.stem.porter import *
from collections import defaultdict

individual_output_file = "data/analysis1.csv"
overall_output_file = "data/analysis2.csv"
distribution_output_file = "data/stem_distribution_analysis.csv"
data_path = "data/trimmed/"
data_files = [data_path+file for file in listdir(data_path)]
print(data_files)
unifier = DataUnifier()
stemmer = PorterStemmer()

def default_value():
    return 0

def clean_outputfile(filename):
    with open(filename, "w+") as file:
        file.write("")

def write_output(filename, output):
    with open(filename, "a") as file:
        file.write(output+"\n")



total_stems = defaultdict(default_value)
#total_words = 0

#clean_outputfile(individual_output_file)
#clean_outputfile(overall_output_file)
clean_outputfile(distribution_output_file)
#write_output(individual_output_file,"File,Words,DistinctStems")
#write_output(overall_output_file,"Words,DistinctStems")
write_output(distribution_output_file,"Occurences,Stems")


for file in data_files:
    #stems = defaultdict(default_value)
    #words = 0
    sentences = unifier.unify_file(file)
    for sentence in sentences:
        for word in sentence.split(" "):
            stem = stemmer.stem(word)
            #stems[stem] = stems[stem] + 1
            total_stems[stem] = total_stems[stem] + 1
            #words += 1
            #total_words += 1
            #total_num_distinct_stems = len(total_stems.keys())
            #csv_line = f"{total_words},{total_num_distinct_stems}"
            #write_output(overall_output_file, csv_line)
    #num_distinct_stems = len(stems.keys())
    print(file)
    #print(f"File: {file}, Words: {words}, Distinct Stems: {num_distinct_stems}")
    #csv_line = f"{file},{words},{num_distinct_stems}"
    #write_output(individual_output_file, csv_line)


occurences = defaultdict(default_value)

for key in total_stems.values():
    occurences[str(key)] = occurences[str(key)] + 1

for num_occurences, num_stems in occurences.items():
    csv_line = f"{num_occurences},{num_stems}"
    write_output(distribution_output_file,csv_line)
