#coding: UTF-8

ans = []
f = open("hightemp.txt","r") 
for line in f:
  ans.append(unicode(line,"utf-8").split())
   
ans.sort(key=lambda x:x[2], )

res18 = open("res18.txt","w")
for i in ans[::-1]:
  res = " ".join(i) + "\n"
  res18.write(res.encode("utf-8"))

f.close()
res18.close()
