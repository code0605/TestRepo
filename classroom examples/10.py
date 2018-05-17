a=[89,45,67,34,90,78]

for x in a:
    print(x)

for x in a:
    print(x,end=" ")

print("_" * 50)

for x in enumerate(a):
    print(x)

for x,y in enumerate(a):
    print(x,y)

for index,value in enumerate(a):
    print("{} is at index {}".format(value,index))
