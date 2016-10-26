
# Import the toolkit and tags
import nltk
import csv
import nltk.corpus
# Import HMM module
from nltk.tag import hmm

mylist = [(char, "") for char in "abc" * 20]
print mylist
exit()
#from nltk.corpus import treebank

#print(str(nltk.corpus.treebank).replace('\\\\','/'))

#
# # Train data - pretagged
# #train_data = treebank.tagged_sents()[:3000]
#
#print train_data[0]
#
# #fname1="trainingDataInputForQn1.txt"
# fname1="corpus_original.txt"
#
#
# # with open('fname1', mode="rU") as infile:
# #     csv_f = csv.reader(infile)
# #     next(csv_f, None)  # skip the headers
# #     for row in csv_f:
# #         row[2:3] = row[2].split(' ')
# #         print row
#
# with open(fname1) as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])
#
#     #    writer = csv.writer(outfile)
#     #    writer.writerow(['dataheader1', 'dataheader2', 'dataheader3', 'dataheader4', 'dataheader5', 'dataheader6', 'dataheader7' etc. ])
#
# #read contents of the training data file
# #f= open(fname1)
# #content = f.read()
#
# print content
#
# exit

#the training and tagging part

s = """"Your humble writer knows a little bit about a lot of things, but despite writing a fair amount about text processing (a book, for example), linguistic processing is a relatively novel area for me. Forgive me if I stumble through my explanations of the quite remarkable Natural Language Toolkit (NLTK), a wonderful tool for teaching, and working in, computational linguistics using Python. Computational linguistics, moreover, is closely related to the fields of artificial intelligence, language/speech recognition, translation, and grammar checking.\nWhat NLTK includes\nIt is natural to think of NLTK as a stacked series of layers that build on each other. Readers familiar with lexing and parsing of artificial languages (like, say, Python) will not have too much of a leap to understand the similar -- but deeper -- layers involved in natural language modeling.\nGlossary of terms\nCorpora: Collections of related texts. For example, the works of Shakespeare might, collectively, by called a corpus; the works of several authors, corpora.\nHistogram: The statistic distribution of the frequency of different words, letters, or other items within a data set.\nSyntagmatic: The study of syntagma; namely, the statistical relations in the contiguous occurrence of letters, words, or phrases in corpora.\nContext-free grammar: Type-2 in Noam Chomsky's hierarchy of the four types of formal grammars. See Resources for a thorough description.\nWhile NLTK comes with a number of corpora that have been pre-processed (often manually) to various degrees, conceptually each layer relies on the processing in the adjacent lower layer. Tokenization comes first; then words are tagged; then groups of words are parsed into grammatical elements, like noun phrases or sentences (according to one of several techniques, each with advantages and drawbacks); and finally sentences or other grammatical units can be classified. Along the way, NLTK gives you the ability to generate statistics about occurrences of various elements, and draw graphs that represent either the processing itself, or statistical aggregates in results.\nIn this article, you'll see some relatively fleshed-out examples from the lower-level capabilities, but most of the higher-level capabilities will be simply described abstractly. Let's now take the first steps past text processing, narrowly construed. """
sentences = s.split('.')[:-1]
seq = [map(lambda x:(x,''), ss.split(' ')) for ss in sentences]
symbols = list(set([ss[0] for sss in seq for ss in sss]))
states = range(5)

#print (symbols)
print(states)
#trainer = nltk.tag.hmm.HiddenMarkovModelTrainer(states=states,symbols=symbols)
#tagger = trainer.train_supervised(seq)

#print tagger.tag("Today is a good day")
#m.random_sample(random.Random(),10)


#tokenize the entire text in training data, not just setences.
# tokens = nltk.word_tokenize(content)
#
#
# print tokens
#
# # Setup a trainer with default(None) values
# # And train with the data
# trainer = hmm.HiddenMarkovModelTrainer()
# tagger = trainer.train_supervised(train_data)
#
# print tagger
# # Prints the basic data about the tagger
#
# print tagger.tag("Today is a good day .".split())
#
# print tagger.tag("Joe met Joanne in Delhi .".split())
#
# print tagger.tag("Chicago is the birthplace of Ginny".split())
