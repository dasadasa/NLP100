#coding: UTF-8
text = "This is a pen"

def cipher(text):
  ans = ""
  for i in text:
    if i.islower():
      str = 219 - ord(i)
      ans += chr(str)
    else:
      ans += i
  return ans

print cipher(text)  
