f=open("c:\\users\\tring\\desktop\\synechron3\\marks.csv","r")
for line in f:
    fields = line.split(",")
    name=fields[0]
    marks=[]
    for x in fields[1:]:
        marks.append(int(x))
    average=sum(marks)/len(marks)

    print("The average of {0} is {1:.2f}".format(name,average))
f.close()
