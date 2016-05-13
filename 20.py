#coding: UTF-8

import json

uk = open("jawiki-uks.txt","w")

with open("jawiki-countrys.json","r") as f:  
  for line in f.readlines(): 
    aa = json.loads(line) 
    if aa["title"] == u"イギリス":
       res =  aa["text"]
       uk.write(res.encode("utf-8"))
