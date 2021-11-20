#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from utils.DataUnifier import DataUnifier
from os import listdir
from nltk.stem.porter import *
from collections import defaultdict
from random import choice

class Heuristics:
    """
    Heuristics:
        - Prevalent: return the most frequently encountered completion
        - Random: return a completion at random
    """
    Prevalent = "Prevalent"
    Random = "Random"


class HeuristicCompletion():
    """
    An extension of the Naive stem completer: 
        - train on text files to create a mapping from stem to completions
        - predict completion as a collection of possible completions given a heuristic
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
                stem_dict = self.stem_completions.get(stem, dict())
                word_count = stem_dict.get(word, 0) + 1
                stem_dict[word] = word_count
                self.stem_completions[stem] = stem_dict

    def predict(self, sentence, heuristic="Prevalent"):
        stems = sentence.split(" ")
        prediction = []
        for stem in stems:
            stem_completions = self.stem_completions.get(stem, False)
            if stem_completions:
                if heuristic == Heuristics.Prevalent:
                    prevalent = max(stem_completions, key=stem_completions.get)
                    prediction.append(prevalent)
                elif heuristic == Heuristics.Random:
                    random_completion = choice(list(stem_completions.keys()))
                    prediction.append(random_completion)
            else:
                prediction.append("___")
        return prediction