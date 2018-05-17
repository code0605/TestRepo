#ping a list of machines
import os
ips=[
"localhost",
"www.google.com",
"www.intel.com",
"www.redbus.in",
"www.trumpputinmodi.com"
]

while True:
	for ip in ips:
		result = os.system("ping {} > NUL".format(ip))
		if result == 0:
			status = "Up"
		else:
			status = "Down"
		print("{} is {}".format(ip,status))
	
	








	