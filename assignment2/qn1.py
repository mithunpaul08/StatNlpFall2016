#-*- coding: utf-8 -*-

import re,os, nltk
fname1="trainingDataInputForQn1.txt"
fname2="trainingDataOutputForQn1.txt"
from nltk.tokenize import sent_tokenize

# write every sentence in a new line into the file
f= open(fname1)
content = f.read()
sent_tokenize_list = sent_tokenize(content)
try:
    os.remove(fname2)
except OSError:
    pass

target = open(fname2, 'a')

for eachLine in sent_tokenize_list:
    combinedText="\n<s>"+eachLine+"</s>\n"
    target.write(combinedText)
target.close()

exit()
