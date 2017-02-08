"""
with open('text_files/pi_digits.txt') as file_object:
	contents = file_object.readlines()
	
pi_string = ''
for line in contents:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))


filename = 'FileWrittingProgramming.py'

with open(filename, 'w') as file_object:
	file_object.write("print('This is like inception!')")

"""

while True:
		
	filename = input("Please enter the desired .txt file that needs word counted: ")

	try:
		with open(str(filename.strip())) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
			pass
	else:
		words = contents.split()
		num_words = len(words)
		
		print("The file: '" + str(filename) + "' has about " + str(num_words) + " words.")
		break
		

