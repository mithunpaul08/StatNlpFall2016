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

#print lambda1
#exit()

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
#print the most common 50 bigrams, but with the frequency counts
#print fdist2.most_common(50)



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
#print the most common 50 bigrams, but with the frequency counts
#print fdist_test_tri.most_common(50)

#for k,v in fdist_test_tri_sorted():
#    print k,v

#m="('the', 'United', 'States')"
# if m in fdist_test_tri.keys():
#      print "unigram word found"
# else:
#     print "given ngram not found"

#if the given ngram in trainign data exists in test data increaes the count of lambda

def lambdaCalculatorForTrigram(word1,word2,word3):
    #return float(fdist_train_tri[word1,word2,word3]) / float(wordCount)
    if (fdist_train_tri[word1,word2,word3] > 0) :
        #print triKeys
        print "trigram word found"
        global lambda3
        lambda3+=1
    elif (fdist_train_bi[word2,word3] > 0):
        print "bigram word found"
        global lambda2
        lambda2+=1
    elif (fdist_train_uni[word3] > 0):
        print "unigram word found"
        global lambda1
        lambda1+=1


#
# for uniKeys in fdist_train_uni.keys():
#     if uniKeys in fdist_test_uni.keys():
#         print uniKeys
#         print "unigram word found"
#         lambda1=lambda1+1
#
# #if the given ngram in trainign data exists in test data increaes the count of lambda
# for biKeys in fdist_train_bi.keys():
#     if biKeys in fdist_test_bi.keys():
#         print biKeys
#         print "bigram word found"
#         lambda2=lambda2+1
#
# #if the given ngram in trainign data exists in test data increaes the count of lambda
# for triKeys in fdist_train_tri.keys():
#     if triKeys in fdist_test_tri.keys():
#         print triKeys
#         print "trigram word found"
#         lambda3=lambda3+1

lambdaCalculatorForTrigram("want","english","food")

print "\n"
print "\nLambda 1:" + `lambda1`
print "\nLambda 2:" + `lambda2`
print "\nLambda 3:" + `lambda3`

#normalizing lambda
sumLambda = lambda1 + lambda2 + lambda3
# print sumLambda
# exit()
nLambda1= float(lambda1)/float(sumLambda)
nLambda2= float(lambda2)/float(sumLambda)
nLambda3= float(lambda3)/float(sumLambda)


print "\n"
print "\n nLambda 1:" + `nLambda1`
print "\n nLambda 2:" + `nLambda2`
print "\n nLambda 3:" + `nLambda3`
