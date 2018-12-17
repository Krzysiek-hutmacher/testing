print ("hellow ROLD!")


import random


squares = [number*number for number in range(1, 10)]
print (squares)

class Dog:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age
    def say_my_name(self):
        return 'Gav Gav, my name is', self.name

bobik = Dog('baron', 22)
print(bobik.say_my_name())
