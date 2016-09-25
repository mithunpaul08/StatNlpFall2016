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
The unigrams thus calculated can be found in the attached herewith file: UniGramOutputForQn3.txt
The bigrams thus calculated can be found in the attached herewith file: BiGramOutputForQn3.txt
The bigrams thus calculated can be found in the attached herewith file: 
TriGramOutputForQn3.txt


——————————————————————————4. Using the held-out corpus calculate s (5pts)


——————————————————————————5. What is the trigram probabilities of i want English food(P(<s> i want English food </s>)) (original andinterpolated probabilities) ? (1pt)

——————————————————————————6. Propose the better algorithm for the interpolation andcalculate their s and the probabilities of the abovesentence. (optional 5pts).


——————————————————————————7. Describe your work (the number of N-grams, the values of s, how to execute yourprograms for steps 3 and 4, etc.) in README.txt (plain text format) within ONE pageMAX and send to jungyeul@email.arizona.edu before 11:00AM on Tuesday, September 27.DO NOT SEND N-GRAM FILES. Use \LING439/539 Assignment #2" as a subject ofthe mail.3 / 3