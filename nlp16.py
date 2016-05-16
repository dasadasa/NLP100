#coding: UTF-8

import sys

argvs = sys.argv[1]
argument = int(argvs)

fileread = open("hightemp.txt","r")
filereadlines = fileread.readlines()  

numoflines = sum(1 for line in open("hightemp.txt")) 
div = numoflines / argument

if (numoflines % argument) == 0:
  for i in xrange(div):
    splitfile = "".join(filereadlines[argument*(i):argument*(i+1)])
    print splitfile
else:
  print "No split by this argument" 

fileread.close()
