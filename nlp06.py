#coding: UTF-8
txt1 = "paraparaparadise"
txt2 = "paragraph"

def ngram(text,n):
  list = []
  if len(text) >= n:
      for i in xrange(len(text) - n + 1):
          list.append(text[i:i+n])
  return list

X = set(ngram(txt1,2))
Y = set(ngram(txt2,2))

print X,Y

print ("wa:%s" % list(X|Y))
print ("seki:%s" % list(X&Y))
print ("sa:%s" % list(X-Y))

print u"\"se\"はXに含まれているか:" 
print "se" in list(X)

print u"\"se\"はYに含まれているか:" 
print "se" in list(Y)
