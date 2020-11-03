#FIRST METHOD
#squares = []
#for value in range(1-11):
#for value in range(11):
#	squares.append(value ** 2)


#SECOND METHOD
#list comprehension
squares = [value**2 for value in range(11)]
print(f"Squares: {squares}")

sum_of_squares = sum(squares)
print(f"Sum: {sum_of_squares}")

million = [value for value in range(1_000_001)]
#for val in million:
#	print(val)
oddNumbers = [val for val in range(1, 20, 2)]
print(f"Odds: {oddNumbers}")

threes = [val for val in range(3, 31, 3)]
print(f"Threes: {threes}")