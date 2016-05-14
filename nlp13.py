#coding: UTF-8

col1 = open("col1.txt")
col2 = open("col2.txt")

with open("merge_col1_col2.txt","w") as f:
  for i,j in zip(col1,col2):
    f.write(i.strip() + "\t" + j.strip() + "\n") 

col1.close
col2.close
