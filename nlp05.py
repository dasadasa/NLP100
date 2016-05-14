#coding: UTF-8
text = "I am an NLPer"

def ngram(text,n):
  list = []
  if len(text) >= n:
      for i in xrange(len(text) - n + 1):
          list.append(text[i:i+n])
  return list

print ngram(text,2)
print ngram(text.split(),2)
