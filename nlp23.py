#coding: UTF-8

import re

with open("jawiki-uks.txt","r") as f:  
  for line in f.readlines(): 
    matchtext = re.match(r"(?P<number>=*)(?P<section>.*)=+$",line)
    if matchtext is not None:
      print "Level:" 
      print (int(line.count("=")/2)-1)
      print "SectionName:"      
      print line
