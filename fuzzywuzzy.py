import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

standard = 'жадина-говядина, турецкий барабан, кто на нем играет - противный таракан'
dic = {}

with open('greedy.csv', newline='', encoding = 'utf 8') as File:
    reader = csv.DictReader(File)
    for row in reader:
        i = row['text'].strip().lower()
        f = int(fuzz.ratio(i, standard))
    print('comparing {0} and {1}; result : {2}'.format(i, standard, f))
    dic[f] = dic.get(f, set()) | set([i])
    for key, values in sorted(d.items(), key=lambda x: -x[0]):
        print(key, values)
