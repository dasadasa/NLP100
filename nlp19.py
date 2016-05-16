#coding: UTF-8
from collections import Counter

ans = []
fileread = open("hightemp.txt","r")

for line in fileread:
  ans.append(line.split()[0])

counter = Counter(ans)
for count,word in counter.most_common():
  print "\t" + count , word

fileread.close()

