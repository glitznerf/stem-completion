#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
import re

class DataUnifier():
    files = []
    output_file = ""
    temp_storage = []

    def __init__(self):
        pass

    def unify_full(self, directory, output):
        self.output_file = output
        self.files = [directory+file for file in listdir(directory)]
        self._clear_outputfile
        self._merge_sentences()

    def unify_file(self, file):
        self.files = [file]
        self._merge_sentences(individual=True)
        return self.temp_storage

    def _clear_outputfile(self):
        with open(self.output_file, "w+") as file:
            return

    def _merge_sentences(self, individual=False):
        for filename in self.files:
            with open(filename, "r", encoding="utf8") as file:
                sentence = ""
                for line in file:
                    line = self._clean_line(line)
                    if line in ["", " "]:
                        self._write_output(sentence, individual)
                        sentence = ""
                    else: 
                        sentence += " "
                        for character in line:
                            if character in ",.?!:;":
                                output = self._clean_line(sentence)
                                self._write_output(output, individual)
                                sentence = ""
                            else: 
                                sentence += character

    def _clean_line(self, line):
        line = line.strip()
        line = line.lower()
        line = re.sub("[^A-Za-z ,.?!:;]", " ", line)
        #line = re.sub(" +", " ", line)
        line = line.split()
        line = " ".join(line)
        return line

    def _write_output(self, sentence, individual):
        validation = sentence.split()
        if len(validation)>0 and validation[0]!= " ":
            if individual:
                self.temp_storage.append(sentence)
                return
            with open(self.output_file, "a+") as output:
                output.write(sentence+"\n")

#unifier = DataUnifier()

#unifier.unify_full("../data/trimmed/","../data/unified/sentences.txt")