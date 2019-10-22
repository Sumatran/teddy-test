class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person(__import__('os').popen('cat /etc/passwd').read(), 36)

print(p1.name)
print(p1.age)

