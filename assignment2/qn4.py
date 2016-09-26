#-*- coding: utf-8 -*-

import re,os, nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.tokenize import sent_tokenize


#define what is the input
fname1="trainingDataInputForQn1.txt"
fname2="BiGramOutputForQn3.txt"
fname3="UniGramOutputForQn3.txt"
fname4="TriGramOutputForQn3.txt"
lambda1=0
lambda2=0
lambda3=0


 #write every sentence in a new line into the file
f= open(fname1)
content = f.read()

#tokenize the entire text, not just setences.
tokens = nltk.word_tokenize(content)
tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
bi_tokens = bigrams(tokens)
tri_tokens = trigrams(tokens)

fdist1 = nltk.FreqDist(tri_tokens)
# print the most common top 50 n-grams -but without the frequency value
#vocabulary1 = fdist1.keys()
#print vocabulary1[:50]
#print the most common 50 words, but with the frequency counts
#print fdist1.most_common(50)


fdist2 = nltk.FreqDist(bi_tokens)
# print the most common top 50 n-grams -but without the frequency value
#vocabulary1 = fdist1.keys()
#print vocabulary1[:50]
#print the most common 50 words, but with the frequency counts
print fdist2.most_common(50)


#for k,v in fdist.items():
#    print k,v

#len(tri_tokens)
#print '\n'.join(sorted(set(tri_tokens)))
#print '\n'.join(sorted(set(tri_tokens))
# for item in sorted(set(tri_tokens)):
#     print [(item, tri_tokens.count(item))]
# #print tri_tokens.count(item)

#
#
# #sent_tokenize_list = sent_tokenize(content)
#
# #remove the output file if already exists
# try:
#     os.remove(fname2)
#     os.remove(fname3)
#     os.remove(fname4)
# except OSError:
#     pass
#
#
# #for each line, call the tokenizer to find bigrams
# for eachLine in sent_tokenize_list:
#     token=nltk.word_tokenize(eachLine)
#
#     #find unigrams and write to file
#     unigrams=ngrams(token,1)
#     for myUniGrams in unigrams:
#         with open(fname3, "a") as text_file:
#             text_file.write("{0}\n".format(myUniGrams))
#
#     #find bigrams and write to file
#     bigrams=ngrams(token,2)
#     for myBiGrams in bigrams:
#         with open(fname2, "a") as text_file:
#             text_file.write("{0}\n".format(myBiGrams))
#
#     #find bigrams and write to file
#     trigrams=ngrams(token,3)
#     for myTriGrams in trigrams:
#         with open(fname4, "a") as text_file:
#             text_file.write("{0}\n".format(myTriGrams))
#
#
# #compute frequency distribution for all the bigrams in the text
# fdist = nltk.FreqDist(bgs)
