#-*- coding: utf-8 -*-

import re,os, nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.tokenize import sent_tokenize
from decimal import Decimal


#fname1="trainingDataInputForQn1.txt"
fname1="trainingDataOutputForQn1.txt"
#read contents of the training data file
f= open(fname1)
content = f.read()

#tokenize the entire text in training data, not just setences.
tokens = nltk.word_tokenize(content)
uni_tokens_training = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
bi_tokens_training = bigrams(uni_tokens_training)

noOfWordTokens= len(tokens)
noOfWordTypes= len(set(tokens))

#tri_tokens_training = trigrams(uni_tokens_training)

#fdist_train_tri = nltk.FreqDist(tri_tokens_training)
fdist_train_bi = nltk.FreqDist(bi_tokens_training)
fdist_train_uni= nltk.FreqDist(uni_tokens_training)


#hardcoding a discount value
delta = 0.000000000000075
lambda2 = 0.00
lambda1 = 0.00
lambdaV=0.000;
uniqueNoOfBigrams=  len(fdist_train_bi.keys())

def calcUniGramCountForKneser(word1):
    myUniCount= float(fdist_train_uni[word1])
    #applying laplace smoothing for unigrams
    #PLaplace(wi) =C(wi) + 1/ (N + V)
    global noOfWordTokens,noOfWordTypes
    return float(myUniCount+1)/float(noOfWordTypes+noOfWordTokens)


def calcBiGramCountForKneser(word1,word2):
    myBiCount= float(fdist_train_bi[word1,word2])
    myUniCount= calcUniGramCountForKneser(word1)
    #applying laplace smoothing for unigrams
    #PLaplace(wi) =C(wn􀀀1wn) + 1/C(wn􀀀1) + V
    global uniqueNoOfBigrams
    return float(myBiCount+1)/float(uniqueNoOfBigrams+myUniCount)
    #return fdist_train_bi[word1,word2]


#lambda calculation
def lambdaCalculatorForKneserBigram(word1,word2):
    global lambdaV;
    if (fdist_train_bi[word1,word2] > 0):
        lambda2= (1+(float(delta)/calcUniGramCountForKneser(word1)))
        lambdaV=lambda2
    return lambdaV

#sentence to calculate interpolation
inputSentence = "<s> i want english food </s>"
tokens_inputSentence = nltk.word_tokenize(inputSentence)
bi_tokens_inputSentence = bigrams(tokens_inputSentence)

#complete formula
#PKN(wi∣wi−1)=max(c(wi−1wi)−δ,0)c(wi−1)+λ∣∣{wi−1:c(wi−1,wi)>0}∣∣∣∣{wj−1:c(wj−1,wj)>0}∣∣
for biGramsInInput in bi_tokens_inputSentence:
    print "\n"+`biGramsInInput`

    #calculate numerator 1-max(c(wi−1wi)−δ,0)
    biGramCountForKneser= calcBiGramCountForKneser(biGramsInInput[0],biGramsInInput[1])
    #print biGramCountForKneser
    n1= max(biGramCountForKneser-delta,0)
    #print n1;

    #calculate denominator 1-max(c(wi−1wi)−δ,0)
    d1= calcUniGramCountForKneser(biGramsInInput[0])
    #print d1

    # calculate pContinuation
    pContinuation = calcBiGramCountForKneser(biGramsInInput[0],biGramsInInput[1])/uniqueNoOfBigrams
    #print pContinuation

    lambdaValue=lambdaCalculatorForKneserBigram(biGramsInInput[0],biGramsInInput[1])
    #normalizing lambda
    #print lambdaValue

    #combine all
    Pkn=(n1/d1)+ (lambdaValue*pContinuation)
    print "value of interpolated probability of the given bi is:" + `Pkn`




exit()
