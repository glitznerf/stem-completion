#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from utils.DataUnifier import DataUnifier
from os import listdir
from nltk.stem.porter import *
from collections import defaultdict
from NaiveCompletion import NaiveCompletion
from HeuristicCompletion import HeuristicCompletion
import random

def clean_outputfile(filename):
    with open(filename, "w+") as file:
        file.write("")

def write_output(filename, output):
    with open(filename, "a") as file:
        file.write(output+"\n")

data_path = "data/trimmed/"
unifier = DataUnifier()
stemmer = PorterStemmer()
naive_output_file = "data/naive_containment_log.txt"
heuristics_output_file = "data/heuristic_evaluation_log.txt"

def get_data():
    data_files = [data_path+file for file in listdir(data_path)]
    num_training_files = 8*len(data_files)//10
    random.shuffle(data_files)
    training_files = data_files[:num_training_files]
    test_sentences = []
    for file in data_files[num_training_files:]:
        test_sentences += unifier.unify_file(file)
    return training_files, test_sentences

def evaluate_naive(training_files, test_sentences):
    naive = NaiveCompletion()

    for file in training_files:
        naive.train(file)

    """
    for sentence in test_sentences:
        stems = " ".join([stemmer.stem(word) for word in sentence.split(" ")])
        prediction = naive.predict(stems)
        contained = []
        for ix, word in enumerate(sentence.split(" ")):
            contained.append(word in prediction[ix])
        print(f"\nSentence '{sentence}' was stemmed to \n\t'{stems}' and predicted as \n\t{prediction}, containment was\n\t{contained}, rate = {contained.count(True)}/{len(contained)}")
    """
    contained,not_contained = 0,0

    for sentence in test_sentences:
        stems = " ".join([stemmer.stem(word) for word in sentence.split(" ")])
        prediction = naive.predict(stems)
        containment = []
        for ix, word in enumerate(sentence.split(" ")):
            containment.append(word in prediction[ix])
        contained += containment.count(True)
        not_contained += containment.count(False)
    
    random.shuffle(test_sentences)

    for sentence in test_sentences[:10]:
        stems = " ".join([stemmer.stem(word) for word in sentence.split(" ")])
        prediction = naive.predict(stems)
        containment = []
        for ix, word in enumerate(sentence.split(" ")):
            containment.append(word in prediction[ix])
        output = f"Example Test sentence: '{sentence}' stemmed to '{stems}', predicted as {prediction} with containment {containment}."
        write_output(naive_output_file, output)

    output = f"{len(test_sentences)} sentences tested. {contained} stem completions were contained in the output, {not_contained} were not."
    write_output(naive_output_file, output)

def evaluate_heuristics(training_files, test_sentences):
    model = HeuristicCompletion()

    for file in training_files:
        model.train(file)

    prev_true, prev_false = 0, 0
    rand_true, rand_false = 0, 0

    for sentence in test_sentences:
        stems = " ".join([stemmer.stem(word) for word in sentence.split(" ")])
        prediction_prevalent = model.predict(stems, heuristic="Prevalent")
        prediction_random = model.predict(stems, heuristic="Random")
        for ix, word in enumerate(sentence.split(" ")):
            if word == prediction_prevalent[ix]:
                prev_true+=1
            else:
                prev_false+=1
            if word == prediction_random[ix]:
                rand_true+=1
            else:
                rand_false+=1
    
    random.shuffle(test_sentences)

    for sentence in test_sentences[:10]:
        stems = " ".join([stemmer.stem(word) for word in sentence.split(" ")])
        prediction_prevalent = model.predict(stems, heuristic="Prevalent")
        prediction_random = model.predict(stems, heuristic="Random")
        output = f"Example Test sentence: '{sentence}' stemmed to '{stems}'\n\tPrevalent Prediction: {prediction_prevalent}, \n\tRandom Prediction: {prediction_random}"
        write_output(heuristics_output_file, output)

    output = f"{len(test_sentences)} sentences tested in total.\n\tChoosing the prevalent completion had a true:false ratio of {prev_true}:{prev_false}\n\tCompletions at random had a true:false ratio of {rand_true}:{rand_false}."
    write_output(heuristics_output_file, output)
    

training_files, test_sentences = get_data()
"""
clean_outputfile(naive_output_file)

for i in range(3):
    evaluate_naive(training_files, test_sentences)
    print("Eval cycle done")
evaluate_naive(training_files, test_sentences)
"""

#clean_outputfile(heuristics_output_file)
evaluate_heuristics(training_files, test_sentences)