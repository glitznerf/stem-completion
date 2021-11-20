#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
import re
from nltk.stem.porter import *
#import sys
#sys.path.append("../")
#from stemmer import Porter

#stemmer = Porter()
stemmer = PorterStemmer()

class FullStemming():
    input_file = ""
    output_file = ""

    def __init__(self):
        pass

    def stem(self, input, output):
        self.input_file = input
        self.output_file = output
        self._clear_outputfile
        self._merge_sentences()

    def _clear_outputfile(self):
        with open(self.output_file, "w+") as file:
            return

    def _merge_sentences(self):
        with open(self.input_file, "r", encoding="utf8") as file:
            for line in file:
                output = self._clean_line(line)
                output = self._stem_line(output)
                self._write_output(output)

    def _clean_line(self, line):
        line = line.strip()
        line = line.lower()
        line = re.sub("[^A-Za-z ,.?!:;]", " ", line)
        #line = re.sub(" +", " ", line)
        line = line.split()
        line = " ".join(line)
        return line

    def _stem_line(self, line):
        line = line.split(" ")
        stemmed_line = []
        for word in line:
            stemmed_word = stemmer.stem(word)
            stemmed_line.append(stemmed_word)
        return " ".join(stemmed_line)

    def _write_output(self, sentence):
        validation = sentence.split()
        if len(validation)>0 and validation[0]!= " ":
            with open(self.output_file, "a+") as output:
                output.write(sentence+"\n")


#stemming = FullStemming()

#stemming.stem("../data/unified/sentences.txt","../data/unified/sentences_stemmed.txt")