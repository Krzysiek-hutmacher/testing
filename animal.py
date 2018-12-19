# -*- coding: utf-8 -*-
class Animal:
    def __init__(self, name):
        self.name = name.title()
        print ('\n\tРодилось животное\n')
    def eat(self):
        return '«Ням-ням»'
    def getName(self):
        return 'my name is %s' %self.name.upper()
    def setName(self, new_name):
        self.name = new_name.title()
    def makeNoise(self):
        return '%s говорит Гррр' %self.name

class Cat(Animal):
    def __init__ (self, name):
        Animal.__init__ (self, name)
        print ('\n\tродился кот\n')
    def makeNoise(self):
        return '%s Говорит Мяу' %self.name

class Dog(Animal):
    def __init__ (self, name):
        Animal.__init__ (self, name)
        print ('\n\tродился dog\n')
    def makeNoise(self):
        return '{} Говорит Gav'.format(self.name)



bobik = Animal('bobik')
print(bobik.name)
print(bobik.eat())
print(bobik.getName())
bobik.setName('karloson')
print(bobik.getName())
print(bobik.makeNoise())

fanny = Cat('fanny')
print(fanny.makeNoise())
fanny.setName('fima')
print(fanny.eat())
print(fanny.getName())

bar = Dog('sharik')
print(bar.makeNoise())
