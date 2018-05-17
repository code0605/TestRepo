
while True:
    name = input("Enter you name")
    if len(name) > 1:
        print("{} is a valid name".format(name))
        break

print("***************************************")

while True:
    name = input("Enter you name")
    if name == "name":
        print("Your name cant be name")
        continue
    elif len(name) > 1:
        print("{} is a valid name".format(name))
        break

    
