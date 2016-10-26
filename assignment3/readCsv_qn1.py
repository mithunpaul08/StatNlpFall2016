import csv

fname1="corpus_forTest.csv"

with open(fname1) as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        #print(','.join(row))
        print (row)

# with open(fname1) as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)
