import datetime

a=datetime.datetime.today()
b=datetime.datetime(1947,8,15)

print((a-b).days)


#parsing dates from strings

mydate = "20Jan2018"

j = datetime.datetime.strptime(mydate,"%d%b%Y")

print(j)
print(j.year)
print(j.month)
