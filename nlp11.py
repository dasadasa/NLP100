#coding: UTF-8

with open("hightemp.txt","r") as f:
  print (f.read()).replace("\t"," ")
