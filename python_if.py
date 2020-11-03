cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


numbers = [val for val in range(1,11)]
for num in numbers:
	#if(num >= 2 and num <=5):
	if(num >= 2 or num <=5):
		print(num)

toppings = ['mushrooms', 'onions', 'becon']
if('mushrooms' in toppings):
	print('yes shrrroms')
elif('mushrooms'  not in toppings):
	print('no shrroomos')