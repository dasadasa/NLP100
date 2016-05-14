#coding: UTF-8

import re

with open("jawiki-uks.txt","r") as f:  
  for line in f.readlines(): 
    if re.search("Category",line):
       print line,

