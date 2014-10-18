#!/usr/bin/env python
#-*-coding:utf-8-*-



import csv
import unicodedata
import string
from parser import parser
file_name = "../../data/train.csv"


spam_reader = parser(file_name)
result = []
dico = {}

def add_to_dict(dico, element):
  try:
    dico[element] += 1
  except:
    dico[element] = 1
  return dico

def max_count(dico):
  maxx = 0
  for key in dico.keys():
    maxx = max(maxx, dico[key])
  return maxx

def dico_to_list(dico):
  l = map(lambda x : [dico[x]], dico)
  return l
  
max_lb = 100000

count = 0
for row in spam_reader:
  for e in row:
    try:
      float(e)
    except:
      if e == "YES" or e == "NO":
        pass
      else:
        dico = add_to_dict(dico, e)
  count += 1

  if count == max_lb:
    break

l = dico_to_list(dico)

print l


output_file = open('result_count.csv', 'w')
a = csv.writer(output_file)
a.writerows(l)
output_file.close()



c = d
