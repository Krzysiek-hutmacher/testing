# -*- coding: utf-8 -*-
"""
1. Напишите код, описывающий класс Animal:
a) Добавьте атрибут имени животного.
b) Добавьте метод eat(), выводящий «Ням-ням».
c) Добавьте методы getName() и setName().
d) Добавьте метод makeNoise(), выводящий «Имя животного говорит Гррр».
e) Добавьте конструктор класса Animal, выводящий «Родилось животное».
2. Пусть Animal будет родительским для класса Cat. Метод makeNoise() класса Cat выводит «Имя животного говорит Мяу». Конструктор класса Cat выводит «Родился кот», а также вызывает родительский конструктор.
3. Пусть Animal будет родительским для класса Dog. Метод makeNoise() для Dog выводит «Имя животного говорит Гав». Конструктор Dog выводит «Родилась собака», а также вызывает родительский конструктор.
4. Основная программа. Код, создающий кота, двух собак и одно простое животное. Дайте имя каждому животному (через вызов методов). Код, вызывающий eat() и makeNoise() для каждого животного.
"""

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
        return '%s Говорит Gav' %self.name



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
