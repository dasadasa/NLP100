#coding: UTF-8
import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = []
anslist = []

for i in text.split():
  if len(i) <= 4:
      anslist.append(i)
  else:
      naka = list(i[1:-1])
      random.shuffle(naka)
      anslist.append(i[0:1] + "".join(naka) + i[-1])

print " ".join(anslist)

 
