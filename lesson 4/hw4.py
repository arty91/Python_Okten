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
# delete all purchases
# cheapest purchase

import json
from typing import TypedDict, List

NoteType = TypedDict('NoteType', {'purchase': str, 'price': int})


class Note:
	def __init__(self, file_name):
		self.__file_name = file_name
		self.__notes: list[NoteType] = []
		try:
			with open(file_name) as file:
				self.__notes: list[NoteType] = json.load(file)
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
		print('List of notes: ')
		for item in self.__notes:
			print(item)

	def sum_prices(self):
		sum_prices = sum(item['price'] for item in self.__notes)
		print(f'Sum of purchases is: {sum_prices}')

	def max_prices(self):
		print('The most expensive purchase is: ')
		print(max(self.__notes, key=lambda item: item['price']))

	def find_by_name(self):
		find_name = input('What is the name of purchase: ')
		for i in self.__notes:
			if i['purchase'].lower() == find_name.lower():
				print(i)
				return
		print('Not found')

	def min_prices(self):
		print('The cheapest purchase is: ')
		print(min(self.__notes, key=lambda item: item['price']))

	def clear_notes(self):
		self.__notes.clear()
		print('List of notes has been cleared.')


note = Note('purchases.json')

while True:
	print('--------------------------------')
	print('1. Create note')
	print('2. Show all notes')
	print('3. Total sum of purchases')
	print('4. The most expensive purchase')
	print('5. Find by name')
	print('6. The cheapest purchase')
	print('7. Clear purchases')
	print('8. exit')
	print('--------------------------------')
	choice = input('Please make a choice: ')
	print('--------------------------------')

	match choice:
		case '1':
			note.add()
		case '2':
			note.show_all_notes()
		case '3':
			note.sum_prices()
		case '4':
			note.max_prices()
		case '5':
			note.find_by_name()
		case '6':
			note.min_prices()
		case '7':
			note.clear_notes()
		case '8':
			break
