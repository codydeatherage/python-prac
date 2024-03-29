import json

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
			return None
	else:
			return username

def get_new_username():
	"""Prompt for new username"""
	username = input("What is your name?")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username
#Load the username, if it has been stored before
#Otherwise, prompt user for username and store it
def greet_user():
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}")
	else:
		username = get_new_username()
		print(f"We'll remember you next time!")

greet_user()