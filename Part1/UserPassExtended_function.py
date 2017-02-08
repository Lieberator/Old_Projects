
#checks the password
def Get_Password(verified_users, username):
	
	for u, p in verified_users.items():
		if u == username:
			password = p['password']
			return password
		else:
			password = 'wrong password'
			return password
	

verified_users = {
	'jlieb' : {
	'password' : 'Tootsie2',
	},
	 'scott18' : {
	 'password': 'Nationals_16'
	},
	'bkelly8' : {
	'password': 'WinstonSucks14'
	},
	'jknapp0824': {
	'password': 'kobe2408'
	},
}

prompt_username = "what is your username: "
prompt_password = "what is your password: "

counter = 0

while (True and counter<3): #three tries to get the right username and password
	username = input(prompt_username)
	password = input(prompt_password)

	if username not in verified_users.keys():
		print("You have to pay to be a verified user to enter, you may not enter until you pay")
		counter += 1
		continue
	else:
		checkpass = Get_Password(verified_users, username)

	if checkpass == 'wrong password': 
		counter += 1
		print("You entered the wrong username/password")
		continue
	else:
		print("Login: successful")
		
	break
	
if counter == 3:
	print("Login: failed")
 


	
