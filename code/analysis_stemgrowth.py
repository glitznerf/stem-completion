#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
#path.join("../utils/")
from utils.DataUnifier import DataUnifier
from os import listdir
from nltk.stem.porter import *
from collections import defaultdict
import random

overall_output_file = "data/total_stems_words.csv"
data_path = "data/trimmed/"
data_files = [data_path+file for file in listdir(data_path)]
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

sentences = []

total_stems = defaultdict(default_value)
total_words = 0

clean_outputfile(overall_output_file)
write_output(overall_output_file,"Words,DistinctStems")

for file in data_files:
    file_sentences = unifier.unify_file(file)
    for sentence in file_sentences:
        sentences.append(sentence)
    print(file)

random.shuffle(sentences)

for ix, sentence in enumerate(sentences):
    for word in sentence.split(" "):
        stem = stemmer.stem(word)
        total_stems[stem] = total_stems[stem] + 1
        total_words += 1
        
        if total_words % 1000 == 0:
            print(f"Sentence {ix} out of {len(sentences)}")
            total_num_distinct_stems = len(total_stems.keys())
            csv_line = f"{total_words},{total_num_distinct_stems}"
            write_output(overall_output_file, csv_line)