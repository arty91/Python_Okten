# найти со списка только уникальные числа
#
# пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]

# def find_only_unique(ls: list):
# 	res = []
# 	duplicates = []
# 	for i in ls:
# 		if i not in res:
# 			res.append(i)
# 		else:
# 			duplicates.append(i)
# 	for i in duplicates:
# 		if i in res:
# 			res.remove(i)
# 	return res
#
#
# print(find_only_unique([1, 2, 3, 4, 2, 5, 1]))


# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон


# class Rectangle:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
#
# 	def __add__(self, other):
# 		return self.x * self.y + other.x * other.y
#
# 	def __sub__(self, other):
# 		return self.x * self.y - other.x * other.y
#
# 	def __lt__(self, other):
# 		return self.x * self.y < other.x * other.y
#
# 	def __gt__(self, other):
# 		return self.x * self.y > other.x * other.y
#
# 	def __eq__(self, other):
# 		return self.x * self.y == other.x * other.y
#
# 	def __ne__(self, other):
# 		return not self.x * self.y == other.x * other.y
#
# 	def __len__(self):
# 		return (self.x + self.y) * 2
#
#
# rectangle1 = Rectangle(1, 7)
# rectangle2 = Rectangle(3, 5)
#
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 < rectangle2)
# print(rectangle1 > rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
#
# print(len(rectangle1))
# print(len(rectangle2))


# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количеств

# from typing import List
#
#
# class Human:
# 	def __init__(self, name, age):
# 		self.age = age
# 		self.name = name
#
#
# class Cinderella(Human):
# 	count = 0
#
# 	def __init__(self, name, age, shoe_size):
# 		super().__init__(name, age)
# 		self.shoe_size = shoe_size
# 		Cinderella.count += 1
#
# 	def __str__(self):
# 		return str(self.__dict__)
#
#
# class Prince(Human):
# 	def __init__(self, name, age, shoe_found):
# 		super().__init__(name, age)
# 		self.shoe_found = shoe_found
#
# 	def find_shoe(self, cinderellas: List[Cinderella]):
# 		for i in cinderellas:
# 			if self.shoe_found == i.shoe_size:
# 				return i
# 		return 'Not found'
#
#
# cinderellas_list = [
# 	Cinderella('Olya', 19, 36),
# 	Cinderella('Kira', 22, 37),
# 	Cinderella('Maya', 28, 34),
# 	Cinderella('Ivana', 18, 35)
# ]
#
# prince = Prince('Oleg', 29, 34)
#
# print(prince.find_shoe(cinderellas_list))
# print(Cinderella.count)
