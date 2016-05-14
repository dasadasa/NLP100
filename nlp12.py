#coding: UTF-8

with open("hightemp.txt","r") as f:    
    col1 = open("col1.txt","w")
    col2 = open("col2.txt","w")
    for line in f:
        col1.write(line.split()[0] + "\n")
        col2.write(line.split()[1] + "\n")
    col1.close()
    col2.close()


