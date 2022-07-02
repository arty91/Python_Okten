# есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com


try:
	with open('emails.txt', 'r') as file1:
		with open('email-gmail.txt', 'w') as file2:
			for i in file1:
				if 'gmail.com' in i:
					file2.write(f'{i}')

except Exception as err:
	print(err)

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

# try:
# 	# gdgdgdg
# 	print(44 / 0)
# except NameError as err:
# 	print(err)
# except ZeroDivisionError as err:
# 	print(err)
# except Exception as err:
# 	print(err)
# else:
# 	print('all right')
# finally:
# 	print('finish')
#
# print('wddwwdmdw')
