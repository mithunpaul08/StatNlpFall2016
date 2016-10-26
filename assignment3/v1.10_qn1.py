#story so far: Code runs for 1000 iterations and tags everything as NOUN. facepalm
#todo in this version:
#1.just experimenting with format of unlabeled



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


#individualSentence1=[("i",""),("like","")]
#individualSentence2=[("apple",""),("pie","")]

#collectionOfSentences=[individualSentence1,individualSentence2]
collectionOfSentences=[]

tags = ["NOUN", "DET"]
symbols = ["a", "b", "c", "x", "y"]
individualSentence=[]

for line in lines:
    #print(line)
    if line != "":
        cols = line.split("\t", 2)
        tags.append(cols[1])

        #print("value of cols[0] is:"+cols[0])
        if(cols[0]==" "):
            #if the value of a symbols is empty, replace it with a temporary value- classifier was giving error
            print("found a symbol that is empty")
            cols[0]="tempWord"
        symbols.append(cols[0])
        wordTuple=[(cols[0],'')]
        individualSentence.append(wordTuple)
        if(cols[0]=='.'):
            #every time you find an end of sentence/period, add it to the collection of sentences
            #print("found an end of sentence")
            collectionOfSentences.append(individualSentence)
            #reset the array so that it can be filled in again with the next sentence
            individualSentence=[]

print("\n")
# #so at this point collectionOfSentences has all the sentences as a list, which inturn is a list of words.
# # also it has a NONE at the end of every word.
#
#print(collectionOfSentences)
# print("\n")
# print(tags)
#
# print("\n")
#print(symbols)
#exit()
    # if line != "":
    #     cols = line.split("\t", 2)
    #     tags.append(cols[1])
    #     symbols.append(cols[0])
    #     individualSentence=[]
    #     individualSentence.append(cols[0])
    #     collectionOfSentences.append(individualSentence)


# print(collectionOfSentences)
# exit()
#
#
# for char in symbols:
#     thisTuple=(char,"")
#     individualSentence1.append(thisTuple)
print("going to train the hmm trainer")
trainer = nltk.tag.HiddenMarkovModelTrainer(tags, symbols)
print("done training the hmm trainer")

#tagger = trainer.train_unsupervised([(char, "") for char in symbols])
print("going to train_unsupervised")
tagger = trainer.train_unsupervised(collectionOfSentences)

print("done with train_unsupervised")
print("going to tag the given sentence")

print(tagger.tag("Today is a good day .".split()))

#right now we need to check if its finding everything as NOUN
#
# symbolsToTest=["four","score","and"]
# for line in lines:
#     cols = line.split("\t", 2)
#     symbolsToTest.append(cols[0])
#     print(tagger.tag(symbolsToTest))
