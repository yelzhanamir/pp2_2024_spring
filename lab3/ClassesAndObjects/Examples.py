#1
class MyClass:
    x=5
p1 = MyClass()
print(p1.x)
#2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#4
class Person:
    def __init__(self, age, name):
     self.age= age
     self.name=name
    def myfunc(self):
       print ("Hello my name is "+self.name)
p1=Person(26,"Yelzhan")
p1.myfunc()
