#coding: UTF-8

import re

with open("jawiki-uks.txt","r") as f:  
  for line in f.readlines(): 
    text = re.search("(File|ファイル):(?P<Filename>.+\..{3})\|",line)
    if text is not None:
       print text.group("Filename")

