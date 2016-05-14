#coding: UTF-8
import sys

argvs = sys.argv[1]

with open("hightemp.txt","r") as f:
  lines = f.readlines()
  for i in range(len(lines)-int(argvs),len(lines)):
      print lines[i],

