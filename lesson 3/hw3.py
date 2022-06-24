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


class Rectangle:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def sum_func(self):
		return self.x * self.y

	def len_func(self):
		return (self.x + self.y) * 2


rectangle1 = Rectangle(1, 7)
rectangle2 = Rectangle(3, 4)

print(rectangle1.sum_func() + rectangle2.sum_func())
print(rectangle1.sum_func() - rectangle2.sum_func())
print(rectangle1.sum_func() == rectangle2.sum_func())
print(rectangle1.sum_func() != rectangle2.sum_func())
print(rectangle1.sum_func() > rectangle2.sum_func())
print(rectangle1.sum_func() < rectangle2.sum_func())

# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количеств
