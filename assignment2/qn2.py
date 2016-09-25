#-*- coding: utf-8 -*-

import re,os, nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize


#define what is the input
#myString= "ftp://www.somewhere.com/over/the/rainbow/image.jpg"
fname1="trainingDataInputForQn1.txt"
fname2="BiGramOutputForQn2.txt"
fname3="UniGramOutputForQn2.txt"
fname4="TriGramOutputForQn2.txt"
#  #text = “this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn.”
# #nltk.download('punkt')
# from nltk.tokenize import sent_tokenize

 #write every sentence in a new line into the file
f= open(fname1)
content = f.read()
sent_tokenize_list = sent_tokenize(content)
# text = inputFile.readlines()

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


#print bigrams to console

#
#
#
# #tokenize each of the sentences
# token=nltk.word_tokenize(text)
# bigrams=ngrams(token,2)
# unigrams=ngrams(token,1)
#
#
# # for myBiGrams in bigrams:
# #     print myBiGrams
#
# #textToWrite='****'.join(bigrams)
# #print textToWrite
#
# #
# #
# #
# #
# #
# #
# # # write every sentence in a new line into the file
# # f= open(fname1)
# # content = f.read()
# # sent_tokenize_list = sent_tokenize(content)
# # #textToWrite='****'.join(sent_tokenize_list)
# # #remove the output file if it exists
# # try:
# #     os.remove(fname2)
# # except OSError:
# #     pass
# #
# # target = open(fname2, 'a')
# #
# # for eachLine in sent_tokenize_list:
# #     combinedText="\n<s>"+eachLine+"</s>\n"
# #     target.write(combinedText)
# # target.close()
# #
# # exit()
# # # #write the stuff to a file
# # # target.write(textToWrite)
# # #
# # # #read that same file and attach a <s> to the begnning and end
# # # #f= open(fname2,'r')
# # # #content = f.read()
# # # with open(fname2) as f:
# # #     content = f.readlines()
# # #
# # # try:
# # #     os.remove("trainingDataOutputForQn1_WithS.txt")
# # # except OSError:
# # #     pass
# # #
# # # target = open("trainingDataOutputForQn1_WithS.txt", 'w')
# # # for eachLine in content:
# # #     #replaceBeginning = re.sub(r'(^)', "<s>", eachLine)
# # #     replaceEnd = re.sub(r'($)', "<s>", eachLine)
# # #     with open("trainingDataOutputForQn1_WithS.txt", "a") as text_file:
# # #         text_file.write("{0}".format(replaceEnd))
# # #
# # #     #with open("Output.txt", "w") as text_file:
# # #     #    print("Purchase Amount: {}".format(TotalAmount), file=text_file)
# # #         #print(replaceBeginning, file=text_file)
# # #     #num = re.sub(r'(^ftp)', "", myString)
# # #     #replaceEnd = re.sub(r'($)', "<s>", replaceBeginning)
# # #     #num = re.sub(r'(^ftp)', "", myString)
# # #     #target.write(replaceBeginning)
# # #
# # # #print replaceEnd
# # #
# # # #target = open("trainingDataOutputForQn1.txt", 'w')
# # # #target.write(textToWrite)
# # # #target.write(sent_tokenize_list)
# # # target.close()
