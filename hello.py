"""
program by hotmathcer
"""


import random


# squares = [number*number for number in range(1, 10)]
# print (squares)
zverinec = []

class Dog:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age
        self.hungry = 100
        zverinec.append(self.name)
        print (self.name, self.age)
    def say_my_name(self):
        self.hungry -= 10
        return 'Gav Gav, my name is', self.name
    def feed(self):
        if self.hungry >=80:
            return "Gav Gav, I'm not hungry"
        elif self.hungry >= 40:
            return "Gav Gav, I'm vary hungry"
        else:
            return "please, I'm die, I want eat"


# bobik = Dog('baron', 22)
# print(bobik.say_my_name())
# print(bobik.say_my_name())
# print(bobik.feed())
# print(bobik.say_my_name())
# print(bobik.say_my_name())
# print(bobik.feed())
# print(bobik.hungry)
#print(zverinec)
