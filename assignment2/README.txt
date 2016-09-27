Note: all the code and output files can be found at the github repository:
https://github.com/mithunpaul08/StatNlpFall2016.git


——————————————————————————

Assumption: the training and test files are renamed as follows and are kept in the same directory:
TrainingDataFile:"trainingDataInputForQn1.txt"
TestDataFile: "testData.txt"


——————————————————————————
Qn 1.Download the training and held-out corpora fromhttps://www.dropbox.com/s/132x4k222wvkf8z/corpus-brown.tar.gz?dl=0 (Brown corpus 50-50)

Ans: done

——————————————————————————
Qn 2. Insert <s> and </s> at the beginning and end of thesentences for your language model (1pt)Ans: Done. I have used the nltk punkt sentence boundary detection. Code can be found in qn2.py attached herewith. THe thus segmented sentences can be found in trainingDataOutputForQn1.txt attached herewith.

——————————————————————————
Qn 3. Using the training corpus find uni, bi, and tri-grams (3pts)

Ans: Done. 

The steps are as follows.
 1) feed the trainingdata to ntlk.sent_tokenize(content) 
2) take each of these sentences and feed it to nltk.word_tokenize(text) 
3) then find bigrams=ngrams(token,2). 
4) calculate the number of bigrams using wc -l


The code can be found in qn3.py attached herewith.
The code can be run by typing “python qn3.py”

The unigrams thus calculated can be found in the attached herewith file: UniGramOutputForQn3.txt
The bigrams thus calculated can be found in the attached herewith file: BiGramOutputForQn3.txt
The bigrams thus calculated can be found in the attached herewith file: 
TriGramOutputForQn3.txt


——————————————————————————4. Using the held-out corpus calculate s (5pts)

Ans: done

The code can be found in the attached file q4.py

The code can be compiled using “python q4.py”

Steps:
4.1. tokenize training data using
tokens = nltk.word_tokenize(content)

4.2. convert to n-grams using corresponding command
Eg:bi_tokens_training = bigrams(uni_tokens_training)

4.3. find a frequency distribution using nltk.FreqDist() :
Eg: fdist_train_tri = nltk.FreqDist(tri_tokens_training)

4.4: for each of the n-gram list in training data, find if the corresponding n-gram exists in test data. If yes, increase the value of lambda by 1
Eg:
for triKeys in fdist_train_tri.keys():
    if triKeys in fdist_test_tri.keys():
        print triKeys

4.5: Normalize lambda using sum of lambdas
Eg:
sumLambda=lambda1+lambda2+lambda3
nLambda1= lambda1/sumLambda

——————————————————————————5. What is the trigram probabilities of i want English food(P(<s> i want English food </s>)) (original andinterpolated probabilities) ? (1pt)

5.a: For calculating the basic probabilities of trigram. 
Refer slide 13 of lecture on sep 6th.
Extrapolating it for trigram probability

P(W| wn-1,wn-2)= c(wn-2 wn-1 wn)/ C(wn-2 wn-1).

Because sum of all trigram counts that starts with a given bigram wn-2wn-1  must be 
same as the number of times the bigram occurs.

Eg: Consider the trigram “I want English”

P(English | want, I)= C(I want English)/C(I want)

Update: I looked up online, and apparently NLTK has modules that does the probability calculations for bigrams[1]. I have extrapolated it for trigrams[2].


References:
1. https://stackoverflow.com/questions/38068539/finding-conditional-probability-of-trigram-in-python-nltk

2. http://www.katrinerk.com/courses/python-worksheets/language-models-in-python
——————————————————————————6. Propose the better algorithm for the interpolation andcalculate their s and the probabilities of the abovesentence. (optional 5pts).


——————————————————————————7. Describe your work (the number of N-grams, the values of s, how to execute yourprograms for steps 3 and 4, etc.) in README.txt (plain text format) within ONE pageMAX and send to jungyeul@email.arizona.edu before 11:00AM on Tuesday, September 27.DO NOT SEND N-GRAM FILES. Use \LING439/539 Assignment #2" as a subject ofthe mail.3 / 3