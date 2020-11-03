#Chapter 8-9
def show_messages(messages):
	for msg in messages:
		print(msg)

msgs = ['hi', 'bye', 'cy@', '234lwoekr134o']
show_messages(msgs)

#8-10
def send_messages(new_msgs, sent_msgs):
	while(new_msgs):
		msg = new_msgs.pop()
		print(msg)
		sent_msgs.append(msg)

new_msgs = msgs[:]
sent_msgs = []
send_messages(new_msgs[:], sent_msgs)

print(f"Messages: {new_msgs}")
print(f"Sent: {sent_msgs}")
print('*' * 50)
def make_pizza(*toppings):
	"""Print the list of requested toppings"""
	for topping in toppings:
		print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'sprinkle', 'mustard')
print('*' * 50)
print('*' * 50)
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', 
				location='princeton', field='physics')

print(user_profile)
