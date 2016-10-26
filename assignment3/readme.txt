Instructions:

To Install nltk using:
sudo pip install -U nltk

To Download treebank corpus:
python -m nltk.downloader treebank

To run my file:
python v1.2_qn1.py

Note: I have implemented the hmm pos tagger from nltk. However, there is something wrong in the way I am preprocessing my data into
the hashmap. My tagger works fine for treebank tagged corpus, but it gives me an error for index out of range. I have spent
more than 12 hours on it, and I give up. Will send an updated version if I can figure this out before the class today.

Error:
File "v1.2_qn1.py", line 42, in <module>
  tagger = trainer.train_supervised(mydata)
File "/Library/Python/2.7/site-packages/nltk/tag/hmm.py", line 1066, in train_supervised
  state = token[_TAG]
IndexError: string index out of range
