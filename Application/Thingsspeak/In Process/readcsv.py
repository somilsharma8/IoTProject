import csv

exfile=open('feeds.csv')
exread=csv.reader(exfile)
exdata=list(exread)
print(exdata)
