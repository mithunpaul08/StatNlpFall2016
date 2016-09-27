#-*- coding: utf-8 -*-

import re,os, nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.tokenize import sent_tokenize
from decimal import Decimal


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
        global lambda3
        lambda3+=1
    elif (fdist_test_bi[word2,word3] > 0):
        global lambda2
        lambda2+=1
    elif (fdist_test_uni[word3] > 0):
        global lambda1
        lambda1+=1


for triKeys in fdist_train_tri.keys():
    lambdaCalculatorForTrigram(triKeys[0],triKeys[1],triKeys[2])

#normalizing lambda
sumLambda = lambda1 + lambda2 + lambda3
nLambda1= float(lambda1)/float(sumLambda)
nLambda2= float(lambda2)/float(sumLambda)
nLambda3= float(lambda3)/float(sumLambda)


############################end of lambda calculation###########




#import data from the sentence end finder qn result
fname1="trainingDataOutputForQn1.txt"
#read contents of the training data file
f= open(fname1)
content = f.read()
tokens = nltk.word_tokenize(content)
uniqueNoOfWords= len(set(tokens))
uni_tokens_training = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
fdist_train_uni= nltk.FreqDist(uni_tokens_training)


# an nltk.FreqDist() is like a dictionary,
# but it is ordered by frequency.
# Also, nltk automatically fills the dictionary
# with counts when given a list of words.


#print the most common 20 unigrams
list(fdist_train_uni.keys())[:20]
fdist_train_uni.most_common(20)

#print bigrams
bi_tokens_training = bigrams(uni_tokens_training)
fdist_train_bi = nltk.FreqDist(bi_tokens_training)
#
# # an nltk.ConditionalFreqDist() counts frequencies of pairs.
# # When given a list of bigrams, it maps each first word of a bigram
# # to a FreqDist over the second words of the bigram.
#

bi_tokens_training = bigrams(uni_tokens_training)
cfreq_brown_2gram = nltk.ConditionalFreqDist(bi_tokens_training)


# # conditions() in a ConditionalFreqDist are like keys()
# # in a dictionary
#
cfreq_brown_2gram.conditions()
#
# # the cfreq_brown_2gram entry for "my" is a FreqDist.
#
cfreq_brown_2gram["i"]
#
# # here are the words that can follow after "my".
# # We first access the FreqDist associated with "my",
# # then the keys in that FreqDist
#
cfreq_brown_2gram["my"].keys()
#
# # here are the 20 most frequent words to come after "my", with their frequencies
#
#print cfreq_brown_2gram["i"].most_common(20)

#
# # an nltk.ConditionalProbDist() maps pairs to probabilities.
# # One way in which we can do this is by using Maximum Likelihood Estimation (MLE)
#
cprob_brown_2gram = nltk.ConditionalProbDist(cfreq_brown_2gram, nltk.MLEProbDist)
#
# # This again has conditions() wihch are like dictionary keys
#
cprob_brown_2gram.conditions()
#
# # Here is what we find for "my": a Maximum Likelihood Estimation-based probability distribution,
# # as a MLEProbDist object.
#
cprob_brown_2gram["my"]
#
# # We can find the words that can come after "my" by using the function samples()
#

#print cprob_brown_2gram["my"].samples()


# # Here is the probability of a particular pair:
#
#
#
#print "\n"
#print cprob_brown_2gram["there"].prob("is")

##
# #####
#
# # We can also compute unigram probabilities (probabilities of individual words)
#
fdist_train_uni= nltk.FreqDist(uni_tokens_training)
# freq_brown_1gram = nltk.FreqDist(brown.words())
#
#len_brown = len(brown.words())


wordCount = len(tokens)
#print "\ntotal number of words in the given corpus is"
#print wordCount

countMy=fdist_train_uni["my"]
##print "\nnumber of times the word my occurs is"
#print float(countMy)

#my_unigram_prob= 100.00000
# my_unigram_prob=float(countMy)/float(wordCount)
# print "\nthe probability of the unigram is "
# print my_unigram_prob


#
#function to calculate the unigram probability
def unigram_prob(word):
    return float(fdist_train_uni[word]) / float(wordCount)
#
#
#
# #############
#
# # The contents of cprob_brown_2gram, all these probabilities, now form a
#
# # trained bigram language model. The typical use for a language model is
#
# # to ask it for the probabillity of a word sequence
#
# # P(how do you do) = P(how) * P(do|how) * P(you|do) * P(do | you)
#
#print "the unigram_prob probability of the given word sequence is \n"
#print unigram_prob("stake")

#prob_sentence = unigram_prob("stake") * float(cprob_brown_2gram["stake"].prob("my")) * float(cprob_brown_2gram["my"].prob("political")) * float(cprob_brown_2gram["political"].prob("career"))

#######all trigram related code begins here############

#to find probability of the given sentence in assignment 2
#DIVIDE the given sentence into trigram sequences. Then call bigram on it?
#
# So for calculating the basic probabilities of trigram. Extrapolating (slide 13 of lecture on sep 6th.) for trigram probability, we get:
#
# P(W| wn-1,wn-2)= c(wn-2 wn-1 wn)/ C(wn-2 wn-1).
#
# Because sum of all trigram counts that starts with a given bigram wn-2wn-1  must be
# same as the number of times the bigram occurs. Is that a correct assumption?
#
# Eg: Consider the trigram “I want English”
#
# P(English | want, I)= C(I want English)/C(I want)
#
#now consider the entire sentence "<s> i want english food </s>"
# This will now be
#
#P=  P(want | i, <s>)*P(English | want, i)*P(food | english, want)*P(</s> | food, english)
#refer slide 12 in lecture sep 6th
# now a trigram probability can be divided down as a function of bigram probability as follows
# brown_trigrams = nltk.trigrams(brown.words())
# condition_pairs = (((w0, w1), w2) for w0, w1, w2 in brown_trigrams)
# cfd_brown = nltk.ConditionalFreqDist(condition_pairs)

#tri_tokens_training = trigrams(uni_tokens_training)
# condition_pairs = (((w0, w1), w2) for w0, w1, w2 in tri_tokens_training)
# cfd_brown = nltk.ConditionalFreqDist(condition_pairs)

#function to return the trigram probability
#P(English | want, I)= C(I want English)/C(I want)

#print the most common 20 trigrams
tri_tokens_training = trigrams(uni_tokens_training)
fdist_train_tri = nltk.FreqDist(tri_tokens_training)
#fdist_train_tri.most_common(20)
#print fdist_train_tri.most_common(20)
#print fdist_train_tri["one","of", "the"]

#for trigrams, break it down to bigram pairs
#brown_trigrams = nltk.trigrams(tokens)
#condition_pairs = (((w0, w1), w2) for w0, w1, w2 in brown_trigrams)
#cfd_tri= nltk.ConditionalFreqDist(condition_pairs)
#print cfd_tri.conditions['be', 'fine']
#float(fdist_train_tri[word]) / float(wordCount)


def trigram_prob(word1,word2,word3):
    #return float(fdist_train_tri[word1,word2,word3]) / float(wordCount)
    biCount= float(fdist_train_bi[word1,word2])
    #print biCount
    triCount= float(fdist_train_tri[word1,word2,word3])
    #print triCount
    #using smoothing
    return (triCount+1)/(biCount+uniqueNoOfWords)

# prob_sentence = trigram_prob("one","of","the")
# print "\n probability of trigram is"
# print prob_sentence

#prob_sentence = trigram_prob("there","is","no")
#* trigram_prob("want","to","show")

prob_sentence = trigram_prob("<s>","i","want") * trigram_prob("i","want","english")  * trigram_prob("want","english","food")  * trigram_prob("english","food","</s>")

#print "the probability of the given word sequence is \n"
#print prob_sentence
#######all trigram related code ends here############


######start of interpolation code##############


def calcInterPolated(word1,word2,word3):
    interPTrigram= nLambda3 * trigram_prob(word1, word2, word3)
    interPBigram=  nLambda2 * cprob_brown_2gram[word2].prob(word3)
    interPUnigram= nLambda1 * unigram_prob(word3)
    return interPTrigram+interPBigram+interPUnigram


inputSentence = "<s> i want english food </s>"
tokens_inputSentence = nltk.word_tokenize(inputSentence)

#uni_tokens_inputSentence = [tokens_inputSentence.lower() for token in tokens if len(token) > 1] #same as unigrams
#bi_tokens_training = bigrams(uni_tokens_training)
tri_tokens_inputSentence = trigrams(tokens_inputSentence)


for triGramsInInput in tri_tokens_inputSentence:
    print "\n"+`triGramsInInput`
    interPForSentence=calcInterPolated(triGramsInInput[0],triGramsInInput[1],triGramsInInput[2])
    print "value of interpolated probability of the given trigram is:" + `interPForSentence`


#interPForSentence=calcInterPolated("i","want","english")
exit()
