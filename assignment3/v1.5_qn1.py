#story so far: code learns and tags single sentences.
#todo in this version:
#1. try to tag entire corpus
#2. try to figure out the unlabeled array format
#

import csv
# Import the toolkit and tags
import nltk
import csv
import nltk.corpus
# Import HMM module
from nltk.tag import hmm


fname1="corpus_forTest.csv"

# with open(fname1) as csvfile:
#     reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
#     print list(reader)
#     your_list = map(tuple, reader)
#.split('\n')

f = open(fname1, "r")
lines = f.read().split("\n") # "\r\n" if needed

tags = ["NNP", "VERB"]
symbols = ["a", "b", "c", "x", "y"]

for line in lines:
    if line != "": # add other needed checks to skip titles
        #print line
        cols = line.split("\t", 2)
        #print cols
        #print cols[1]
        tags.append(cols[1])
        symbols.append(cols[0])
        #unlabeled.append((cols[0], None))
        #print cols


#print tags
#print symbols
#unlabeled = [(char, "") for char in "abc" * 20]
#unlabeled=[[(char, "") for char in "abc" * 20],[(char, "") for char in "xy" * 20]
#print mylist

#print unlabeled

#exit()

#exit()

#
# with open(fname1) as csvfile:
#     reader = csv.reader(csvfile, delimiter='\t')
#     for row in reader:
#         #content=row.split('\t')
#         #print content
#         print '---------'.join(row)

#exit()

#tags = ["NNP", "VERB"]
#symbols = ["a", "b", "c", "x", "y"]
trainer = nltk.tag.HiddenMarkovModelTrainer(tags, symbols)
#tagger = trainer.train_unsupervised(unlabeled, max_iterations=1000)
#tagger = trainer.train_unsupervised(unlabeled)

# believe what fixed the keyErrors for me was getting the data in the right format,
#which ended up being a list of lists of tuples, if that makes sense.
#So... [[(word, None), (word, None), ...], [(word, None), (word, None), ...], ...]
#where each interior list is a sentence out of corpus.it.
# suppose we have 2 sentences 1. i am having a good day 2. i love america.
#the list will be
#[[(i,None),(am,None),(having,None),(a,None),(good,None),(day,None)],[(i,None),(love,None),(america,None)]]

#unlabeled=[[('i',None),(am,None),(having,None),(a,None),(good,None),(day,None)],[(i,None),(love,None),(america,None)]]

word= "apple"
unlabeled=[[(word, None), (word, None)], [(word, None), (word, None)]]


#unlabeled= [('l', ''),('p', ''),('a', '')]

#unlabeled= ([[(char, "") for char in "abc" * 20], [(char, "") for char in "xy" * 20]])
#unlabeled= [[("a", "")],[("x","")]]
#unlabeled = [5, 6, 6, 6, 6, 6, 6, 2, 2, 2, 2, 2, 2, 4, 4, 4]
#unlabeled= [('a', None), ('b', None)]
tagger = trainer.train_unsupervised(unlabeled,max_iterations=1000)



# this works- though i cant figure out how/why
# tagger = trainer.train_unsupervised([
#     [(char, "") for char in "abc" * 20],
#     [(char, "") for char in "xy" * 20]],max_iterations=1000)

print(tagger.best_path(list("abcabc")))
print(tagger.tag("Today is a good day .".split()))

# for line in lines:
#     print(line)
#     tagger.tag(line)



# sentence.append((word, None))
#
# [2:40]
# so None is working for me

# # symbols=['MITHUN','love']
# # unlabeled= [('MITHUN', None), ('love', None)]
# # tags=['NNP','VERB']
# trainer = nltk.tag.HiddenMarkovModelTrainer(tags, list(symbols))
#tagger = trainer.train_unsupervised(unlabeled, max_iterations=1000)

#bring in the hmm tagger


# Setup a trainer with default(None) values
# And train with the data
#trainer = hmm.HiddenMarkovModelTrainer(your_list)
#tagger = trainer.train_supervised(your_list)



#print tagger
# Prints the basic data about the tagger
