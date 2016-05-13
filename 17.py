#coding: UTF-8

ans = []
f = open("hightemp.txt","r") 
for line in f:
  ans.append(unicode(line,"utf-8").split()[0])
  moji = set(ans)

for i in moji:
    print i 
     
f.close()


   
