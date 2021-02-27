class Human:
	name = None
	age = None
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __del__(self):
		print("Destroyed Human")
type1 = Human("Kabbo",22)
print(type1.name,type1.age)