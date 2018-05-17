f=open("c:\\users\\tring\\desktop\\synechron3\\input.txt","r")

lines=f.readlines()

#print(lines[::2])

for line in lines[::2]:
    print(line.rstrip())

f.close()
