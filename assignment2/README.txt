Note: all the code and output files can be found at my github repository:
https://github.com/mithunpaul08/StatNlpFall2016.git


——————————————————————————

Assumption: the training and test files are renamed as follows and are kept in the same directory:
TrainingDataFile:"trainingDataInputForQn1.txt"
TestDataFile: "testData.txt"


——————————————————————————
Qn 1.Download the training and held-out corpora fromhttps://www.dropbox.com/s/132x4k222wvkf8z/corpus-brown.tar.gz?dl=0 (Brown corpus 50-50)

Ans: done

——————————————————————————
Qn 2. Insert <s> and </s> at the beginning and end of thesentences for your language model (1pt)Ans: Done. I have used the nltk punkt sentence boundary detection. Code can be found in qn2.py attached herewith. 

THe thus segmented sentences can be found in trainingDataOutputForQn1.txt attached herewith.

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

no of unigrams:315584

The bigrams thus calculated can be found in the attached herewith file: BiGramOutputForQn3.txt

no of bigrams: 302142

The bigrams thus calculated can be found in the attached herewith file: 
TriGramOutputForQn3.txt

no of trigrams:288748

——————————————————————————4. Using the held-out corpus calculate s (5pts)

Ans: done

The code can be found in the attached file qn4.py

The code can be compiled using “python qn4.py”

Steps:
4.1. tokenize training data using
tokens = nltk.word_tokenize(content)

4.2. convert to n-grams using corresponding command
Eg:bi_tokens_training = bigrams(uni_tokens_training)

4.3. find a frequency distribution using nltk.FreqDist() :
Eg: fdist_train_tri = nltk.FreqDist(tri_tokens_training)

4.4: for each of the n-gram list in training data, find if the corresponding n-gram exists in test data. If yes, increase the value of lambda by 1
Eg:
    if (fdist_test_tri[word1,word2,word3] > 0) :
        #print triKeys
        print "trigram word found"
        global lambda3
        lambda3+=1
    elif (fdist_test_bi[word2,word3] > 0):
        print "bigram word found"
        global lambda2
        lambda2+=1
    elif (fdist_test_uni[word3] > 0):
        print "unigram word found"
        global lambda1
        lambda1+=1

4.5: Normalize lambda using sum of lambdas
Eg:
sumLambda=lambda1+lambda2+lambda3
nLambda1= lambda1/sumLambda


Output from code:

Lambda 1:251458

Lambda 2:171727

Lambda 3:24579



 nLambda 1:0.5615860140609785

 nLambda 2:0.38352122993362575

 nLambda 3:0.0548927560053957
——————————————————————————5. What is the trigram probabilities of i want English food(P(<s> i want English food </s>)) (original andinterpolated probabilities) ? (1pt)

5.a: For calculating the basic probabilities of trigram. 
Refer slide 13 of lecture on sep 6th.
Extrapolating it for trigram probability

P(W| wn-1,wn-2)= c(wn-2 wn-1 wn)/ C(wn-2 wn-1).

Because sum of all trigram counts that starts with a given bigram wn-2wn-1  must be 
same as the number of times the bigram occurs.

Eg: Consider the trigram “I want English”

P(English | want, I)= C(I want English)/C(I want)

 apparently NLTK has modules that does the probability calculations for bigrams. I have extrapolated it for trigrams.

Update: I gave the below sentence to my code. Got a division by zero error.

prob_sentence = trigram_prob("<s>","i","want") * trigram_prob("i","want","english")  * trigram_prob("want","english","food")  * trigram_prob("english","food","</s>")


Since the phrases are not there in the text, I need to replace the hapax legmemnon with “unk”

update: used laplace smoothing

The uniqueNoOfWords/wordTypes were calculated as:

uniqueNoOfWords= len(set(tokens))


Output from code:
the probability of the given word sequence is 
4.57191756316e-19

——————————————————————————

5.b: Use interpolation

Ans:

Since slide12 of lecture sep13 says the sum of lambda values must be 1, am assuming its talking about normalized lambda values.

Code for the same can be found in the attached file qn5b.py

This can be run using the command: python qn5b.py

inputSentence = "<s> i want english food </s>"

Output of the file run on the input sentence is as follows:

('<', 's', '>')
value of interpolated probability of the given trigram is:1.427380086990553e-06

('s', '>', 'i')
value of interpolated probability of the given trigram is:1.427380086990553e-06

('>', 'i', 'want')
value of interpolated probability of the given trigram is:8.953234406465877e-05

('i', 'want', 'english')
value of interpolated probability of the given trigram is:0.00010587439383471013

('want', 'english', 'food')
value of interpolated probability of the given trigram is:6.253243574892173e-05

('english', 'food', '<')
value of interpolated probability of the given trigram is:1.427380086990553e-06

('food', '<', '/s')
value of interpolated probability of the given trigram is:0.018565285394962296

('<', '/s', '>')
value of interpolated probability of the given trigram is:1.427380086990553e-06
——————————————————————————
6.a Propose the better algorithm for the interpolation andcalculate their s and the probabilities of the abovesentence. (optional 5pts).

Ans:

I did some reading and below are the shortlisted interpolated algorithms which I feel will work better than linear interpolation. Infact witted-bell has a higher perplexity of all for bigrams.



1. interpolation with context conditioned weights [2]

Pˆ(wn|wn−2wn−1) = λ1(w
n−1
n−2
)P(wn|wn−2wn−1)
+λ2(w
n−1
n−2
)P(wn|wn−1)
+λ3(w


2. Knesser-Ney interpolated [ref 4, ref 1 eon 4.33]

 
equation for interpolated absolute discounting applied to bigrams:
PAbsoluteDiscounting(wi
|wi−1) = C(wi−1wi)−d
C(wi−1)
+λ(wi−1)P(wi) (4.28)
The first term is the discounted bigram, and the second term the unigram w

PKN(wi∣wi−1)=max(c(wi−1wi)−δ,0)c(wi−1)+λ∣∣{wi−1:c(wi−1,wi)>0}∣∣∣∣{wj−1:c(wj−1,wj)>0}∣∣
PKN(wi∣wi−1)=max(c(wi−1wi)−δ,0)c(wi−1)+λ|{wi−1:c(wi−1,wi)>0}||{wj−1:c(wj−1,wj)>0}|




3.Jelinek-Mercer smoothing (interpolation)[Ref 1- page 15]

4. Modified Interpolated Knesser-Ney by Chen & Goodman made interpolated version [2]

5. Absolute discounting [Ref 2- page 17]

6. Witten -Bell Smoothing [Ref 3- page31]

——————————————————————————
6.b calculate their s and the probabilities of the abovesentence. (optional 5pts).

Ans: I have decided to implement Knesser Ney as given in [4]

The code is attached herewith in the file:qn6.py

Note: I have implemented it for a bigram model.

The results are as follows:

mithuns-MacBook-Pro.local:/Users/mithun/agro/statNlpFall2016/assignment2$ python qn6.py 

('<', 's')
value of interpolated probability of the given bi is:0.9571961601598713

('s', '>')
value of interpolated probability of the given bi is:0.9571961601598713

('>', 'i')
value of interpolated probability of the given bi is:0.9571961601598713

('i', 'want')
value of interpolated probability of the given bi is:0.9571961601598713

('want', 'english')
value of interpolated probability of the given bi is:0.023657569268651087

('english', 'food')
value of interpolated probability of the given bi is:0.019981055123571637

('food', '<')
value of interpolated probability of the given bi is:0.03399076044902431

('<', '/s')
value of interpolated probability of the given bi is:0.9571961601598713

('/s', '>')
value of interpolated probability of the given bi is:0.00011318110179005249
——————————————————————————

References:

1.http://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf
2.https://lagunita.stanford.edu/c4x/Engineering/CS-224N/asset/slp4.pdf (Jurafsky martin text book)
3.http://www.statmt.org/book/slides/07-language-models.pdf
4.http://www.foldl.me/2014/kneser-ney-smoothing/