f=open("c:\\users\\tring\\desktop\\synechron3\\input.txt","r")

for line in f:
    #print(line,end="")
    print(line.rstrip())

f.close()
