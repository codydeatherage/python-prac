#10-3
#name = input("What is your name?")
#filename = 'guest.txt'
#with open('text_files/' + filename, 'w') as file_object:
#	file_object.write(name)

#10-4
filename = 'guest.txt'
with open('text_files/' + filename, 'a') as file_object:
		file_object.write('\n')
while(True):
	name = input("What is your name?")
	greeting = "Hello, " + name
	print(greeting)
	with open('text_files/' + filename, 'a') as file_object:
		file_object.write(name.title() + ' visited!\n')

