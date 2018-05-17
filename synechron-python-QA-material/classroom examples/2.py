name   = input("Please enter your name : ")
height = input("Please enter your height : ")
weight = input("Please enter your weight : ")

print("Your name is, ",name, "height is ",height)

bmi = int(weight) / ((int(height)/100) ** 2)

print("Your bmi is %f" % bmi)
print("Your bmi is %d" % bmi)
print("Your bmi is %s" % bmi)
print("Your bmi is ", round(bmi,2))

if bmi < 18.5 :
    print("You are underweight")
elif bmi > 18.5 and bmi < 24.9 :
    pass
elif bmi > 24.9 and bmi < 30 :
    print("You are overweight")
else:
    print("You are obese")
