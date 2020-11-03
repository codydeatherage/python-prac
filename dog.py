class Dog:
	"""its a dog"""
	def __init__(self, name , age):
		"""init name and attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""make dog sit"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""make dog roll over"""
		print(f"{self.name} rolled over!")

my_dog = Dog('Dave', 6)
my_dog.sit()
my_dog.roll_over()