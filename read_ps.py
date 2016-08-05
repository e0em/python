import getpass
dict={}
reinput_password = False
login_times = 0
f = open ("passwd") 
for line in f.readlines():
	dict[line.split(":")[0]]=line.strip().split(":")[1]
f2 = open("lockuser")
for line2 in f2.readlines():
	dict[line2.strip()]="Locked"
while True:
	if reinput_password == False:
		username = input("input your name??中文:")
	password = getpass.getpass("Input your password:")
	if dict.get(username) == password:
		print("Login success. The secret is 4830")
		reinput_password = False
	elif dict.get(username) == None:
		print("User not exist")
		reinput_password = False
	elif dict.get(username) == "Locked":
		print("you are locked")
	else :
		print("Wrong Password")
		login_times = login_times + 1 
		print("You left %d times to login" % (3 - login_times))
		if login_times >= 3 :
			print("you are locked, please contact system Admin")
			login_times = 0
			dict[username] = "Locked"
			reinput_password = False
			f2 = open("lockuser", mode='a')
			f2.write(username + "\n")
			f2.close()
		else :
			reinput_password = True
