class Animal:
	name = None
	age = None
	def __init__(self,name,age):
		self.name = name
		self.age = age

class Human(Animal):
	profession = None
	def setProfession(self,profession):
		self.profession = profession

humanType1 = Human("Kabbo",22)
humanType1.setProfession("Student")
print(humanType1.name,humanType1.age,humanType1.profession)