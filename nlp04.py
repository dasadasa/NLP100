text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

num = [1,5,6,7,8,9,15,16,19] 
dic = {}

for (i,x) in enumerate(text.split(),1):
  if i in num:
    dic[x[0:1]] = i
  else:
    dic[x[0:2]] = i

print dic 
