import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.tokenize import sent_tokenize
from decimal import Decimal

#import data from the sentence end finder qn result
fname1="trainingDataOutputForQn1.txt"
#read contents of the training data file
f= open(fname1)
content = f.read()
tokens = nltk.word_tokenize(content)
uni_tokens_training = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
fdist_train_uni= nltk.FreqDist(uni_tokens_training)


# an nltk.FreqDist() is like a dictionary,
# but it is ordered by frequency.
# Also, nltk automatically fills the dictionary
# with counts when given a list of words.

#freq_brown = nltk.FreqDist(brown.words())

list(fdist_train_uni.keys())[:20]
fdist_train_uni.most_common(20)

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
print cfreq_brown_2gram["my"]
#
# # here are the words that can follow after "my".
# # We first access the FreqDist associated with "my",
# # then the keys in that FreqDist
#
cfreq_brown_2gram["my"].keys()
#
# # here are the 20 most frequent words to come after "my", with their frequencies
#
print cfreq_brown_2gram["my"].most_common(20)

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
print "\n"
print cprob_brown_2gram["my"].prob("own")

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
print "total number of words in the given corpus is\n"
print wordCount

countMy=fdist_train_uni["my"]
print "number of times the word my occurs is\n"
print float(countMy)

my_unigram_prob= 100.00000
my_unigram_prob=float(countMy)/float(wordCount)
print "the probability of the unigram is \n"
print my_unigram_prob


exit()
#
#function to calculate the unigram probability
# def unigram_prob(word):
#
# #return freq_brown_1gram[ word] / len_brown
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
# prob_sentence = unigram_prob("how") * cprob_brown_2gram["how"].prob("do") * cprob_brown_2gram["do"].prob("you") * \
#
# cprob_brown_2gram["you"].prob("do")
#
# # result: 1.5639033871961e-09
