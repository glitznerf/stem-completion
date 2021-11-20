#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from utils.DataUnifier import DataUnifier
from os import listdir
from nltk.stem.porter import *
from collections import defaultdict

class NaiveCompletion():

    """
    A Naive stem completer: 
        - train on text files to create a mapping from stem to completions
        - predict completion as a collection of possible completions given the training data
    """

    stem_completions = dict()
    stemmer = PorterStemmer()
    unifier = DataUnifier()

    def train(self, filename):
        file_sentences = self.unifier.unify_file(filename)
        for sentence in file_sentences:
            for word in sentence.split(" "):
                if len(word) == 0:
                    continue
                stem = self.stemmer.stem(word)
                stem_set = self.stem_completions.get(stem, set())
                stem_set.add(word)
                self.stem_completions[stem] = stem_set

    def predict(self, sentence):
        stems = sentence.split(" ")
        prediction = [list(self.stem_completions.get(stem,set())) for stem in stems]
        return prediction