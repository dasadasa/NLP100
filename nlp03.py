#coding: UTF-8
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.replace(',',"")
s = s.replace('.',"")
list =[]

for i in s.split(): 
   list.append(len(i))

print list
