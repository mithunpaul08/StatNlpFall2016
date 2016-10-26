#story so far: tagger works, except that for some reason its tagging everything as NOUN.
#todo in this version:
#1. make unlabeled create automatically from this [(char, "") for char in symbols],
#2: try to give an input of collection of sentences to tag? though i doubt its going to make any difference to it
#tagging everything as NOUN...its doing that even for that one line sentence "TOday is a good day"



import csv
# Import the toolkit and tags
import nltk
import csv
import nltk.corpus
# Import HMM module
from nltk.tag import hmm


fname1="corpus_forTest.csv"
f = open(fname1, "r")
lines = f.read().split("\n") # "\r\n" if needed



tags = ["NOUN", "DET"]
symbols = ["a", "b", "c", "x", "y"]

for line in lines:
    if line != "": # add other needed checks to skip titles
        cols = line.split("\t", 2)
        tags.append(cols[1])
        symbols.append(cols[0])


trainer = nltk.tag.HiddenMarkovModelTrainer(tags, symbols)

# tagger = trainer.train_unsupervised([
#     [(char, "") for char in "abc" * 20],
#     [(char, "") for char in "xy" * 20]],max_iterations=1000)

tagger = trainer.train_unsupervised([[(char, "") for char in symbols],[(char, "") for char in "xy" * 20]],max_iterations=1000)

print(tagger.tag("Today is a good day .".split()))

exit()
symbolsToTest=["four","score","and"]
for line in lines:
    #print(line)
    cols = line.split("\t", 2)
    symbolsToTest.append(cols[0])
    #print(symbolsToTest)

print(tagger.tag(symbolsToTest))
