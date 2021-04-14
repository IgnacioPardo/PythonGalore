from pprint import pprint
import pickle
filename = 'dataOutput.pickle'
infile = open(filename,'rb')
data = pickle.load(infile)
infile.close()

rows = [[key, data[key][1], data[key][0][0], data[key][0][2]]+list(data[key][0][1]) for key in data.keys() if len(data[key][0]) > 1]
max_genres = max(map(len, rows))
first_row = ['Title', 'Ammount', 'Certification', 'Year']+ ['Genre_' + str(i+1) for i in range(max_genres-4)]
rows.insert(0, first_row)

import csv

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)