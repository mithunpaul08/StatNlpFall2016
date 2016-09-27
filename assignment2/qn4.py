#-*- coding: utf-8 -*-

import re,os, nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.tokenize import sent_tokenize


#define what is the input
fname1="trainingDataInputForQn1.txt"
fname2= "testData.txt"
lambda1=1
lambda2=1
lambda3=1


#read contents of the training data file
f= open(fname1)
content = f.read()

#tokenize the entire text in training data, not just setences.
tokens = nltk.word_tokenize(content)
uni_tokens_training = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
bi_tokens_training = bigrams(uni_tokens_training)
tri_tokens_training = trigrams(uni_tokens_training)

fdist_train_tri = nltk.FreqDist(tri_tokens_training)
fdist_train_bi = nltk.FreqDist(bi_tokens_training)
fdist_train_uni= nltk.FreqDist(uni_tokens_training)



#################end of training data manipulations#############

 #read contents of the training data file
f2 = open(fname2)
content_test = f2.read()
#tokenize the entire text in test data, not just setences.
tokens_testing = nltk.word_tokenize(content_test)
uni_tokens_testing = [token_testing.lower() for token_testing in tokens_testing if len(token_testing) > 1] #same as unigrams
bi_tokens_testing = bigrams(tokens_testing)
tri_tokens_testing = trigrams(tokens_testing)

fdist_test_tri = nltk.FreqDist(tri_tokens_testing)
fdist_test_bi = nltk.FreqDist(bi_tokens_testing)
fdist_test_uni= nltk.FreqDist(uni_tokens_testing)

def lambdaCalculatorForTrigram(word1,word2,word3):
    if (fdist_test_tri[word1,word2,word3] > 0) :
        #print triKeys
        print "trigram word found"
        global lambda3
        lambda3+=1
    elif (fdist_test_bi[word2,word3] > 0):
        print "bigram word found"
        global lambda2
        lambda2+=1
    elif (fdist_test_uni[word3] > 0):
        print "unigram word found"
        global lambda1
        lambda1+=1


for triKeys in fdist_train_tri.keys():
    print triKeys
    lambdaCalculatorForTrigram(triKeys[0],triKeys[1],triKeys[2])

print "\n"
print "\nLambda 1:" + `lambda1`
print "\nLambda 2:" + `lambda2`
print "\nLambda 3:" + `lambda3`

#normalizing lambda
sumLambda = lambda1 + lambda2 + lambda3
nLambda1= float(lambda1)/float(sumLambda)
nLambda2= float(lambda2)/float(sumLambda)
nLambda3= float(lambda3)/float(sumLambda)


print "\nnLambda 1:" + `nLambda1`
print "\nnLambda 2:" + `nLambda2`
print "\nnLambda 3:" + `nLambda3`
