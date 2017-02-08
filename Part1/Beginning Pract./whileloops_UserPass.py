"""
message = input("Tell me something, and I'll repeat it back to you: ")

print(message)

age = input("Please enter your age: ")
age = int(age)

while(age <18):
	print("You are only: " + str(age) +", you must wait until your 18")
	age+=1
	
print("Finally you are " + str(age) + "! You may enter.")


request = ''
todo_list= []
counter = 0

while request != 'quit':
	request = input("What do you need to do today? (enter 'quit' to exit) ")
	todo_list.append(request)
	

del todo_list[-1]

print("\nTodo list:\n ")
for item in todo_list:
	counter += 1 
	print("\t"+ str(counter) + ".) " + str(item))
"""

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
		for u, p in verified_users.items():
			if u == username:
				checkpass = p['password']

	if checkpass != password: 
		counter += 1
		print("You entered the wrong username/password")
		continue
	else:
		print("Login: successful")
		
	break
	
if counter == 3:
	print("Login: failed")
 
	





