# есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com


# try:
# 	with open('emails.txt', 'r') as file1:
# 		with open('email-gmail.txt', 'w') as file2:
# 			for i in file1:
# 				if '@gmail.com' in i:
# 					file2.write(f'{i.split()[-1]}\n')
#
# except Exception as err:
# 	print(err)

# 2) для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

import json
from typing import TypedDict, List

NoteType = TypedDict('NoteType', {'purchase': str, 'price': int})


class Note:
	def __init__(self, file_name):
		self.__file_name = file_name
		self.__notes: List[NoteType] = []
		try:
			with open(file_name) as file:
				self.__notes: List[NoteType] = json.load(file)
		except:
			pass

	def add(self):
		try:
			with open(self.__file_name, 'w') as file:
				purchase = input('What would you like to buy: ')
				price = ''
				while not price.isdigit():
					price = input('What is the price: ')
				self.__notes.append({'purchase': purchase, 'price': int(price)})
				json.dump(self.__notes, file)
		except:
			print('Something went wrong')

	def show_all_notes(self):
		if not self.__notes:
			print('List of notes is empty')
			return
		for item in self.__notes:
			print(item)

	def sum_prices(self):
		sum_prices = sum(item['price'] for item in self.__notes)
		print(f'{sum_prices=}')

	def max_prices(self):
		print(max(self.__notes, key=lambda item['price']))

	def find_by_name(self):
		find_name = input('What is the name of purchase: ')
		for i in self.__notes:
			if i['purchase'].lower() == find_name.lower():
				print(i)
				return
		print('Not found')

note = Note('purchases.json')

while True:
	print('Create note')
	print('Show all notes')
	print('Total sum of purchases')
	print('The most expensive purchase')
	print('Find by name')
	print('exit')

	choice = input('Please make a choice: ')

	match choice:
		case 1:
			note.add()
		case 2:
			note.show_all_notes()
		case 3:
			note.sum_prices()
		case 4:
			note.max_prices()
		case 5:
			note.find_by_name()
		case 6:
			break
