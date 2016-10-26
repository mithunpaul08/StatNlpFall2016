#story so far: I gave teh input collection as symbols.none . Now The tagger is doing something long.
#todo in this version:
#1.remove the exit() and feed it the entire corpus for tagging.



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

tagger = trainer.train_unsupervised([[(char, "") for char in symbols]])


print(tagger.tag("Today is a good day .".split()))

symbolsToTest=["four","score","and"]
for line in lines:
    #print(line)
    cols = line.split("\t", 2)
    symbolsToTest.append(cols[0])
    #print(symbolsToTest)

print(tagger.tag(symbolsToTest))
