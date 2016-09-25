#-*- coding: utf-8 -*-

import re,os, nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize


#define what is the input
fname1="trainingDataInputForQn1.txt"
fname2="BiGramOutputForQn3.txt"
fname3="UniGramOutputForQn3.txt"
fname4="TriGramOutputForQn3.txt"

 #write every sentence in a new line into the file
f= open(fname1)
content = f.read()
sent_tokenize_list = sent_tokenize(content)

#remove the output file if already exists
try:
    os.remove(fname2)
    os.remove(fname3)
    os.remove(fname4)
except OSError:
    pass

#for each line, call the tokenizer to find bigrams
for eachLine in sent_tokenize_list:
    token=nltk.word_tokenize(eachLine)

    #find unigrams and write to file
    unigrams=ngrams(token,1)
    for myUniGrams in unigrams:
        with open(fname3, "a") as text_file:
            text_file.write("{0}\n".format(myUniGrams))

    #find bigrams and write to file
    bigrams=ngrams(token,2)
    for myBiGrams in bigrams:
        with open(fname2, "a") as text_file:
            text_file.write("{0}\n".format(myBiGrams))

    #find bigrams and write to file
    trigrams=ngrams(token,3)
    for myTriGrams in trigrams:
        with open(fname4, "a") as text_file:
            text_file.write("{0}\n".format(myTriGrams))
