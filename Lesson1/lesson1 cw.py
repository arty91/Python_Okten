'''
створити пустый список users_list = []

стврорити меню в якому потрібно реалізувати:

1) додававання нового юзера
2) вивід всіх юзерів
3) вивід всіх юзерів за віком
4) видалення юзера по id
5) заміна статуса юзера на протилежний
6) вихід з меню

приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}
'''

from uuid import uuid4

users_list = []

menu_options = {
    1: 'Add a new User',
    2: 'Show all users',
    3: 'Show all users by Age',
    4: 'Delete User by ID',
    5: 'Change User Status to opposite by ID',
    6: 'Exit menu',
}
print('--------------------------------------------')


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    id = str(uuid4())
    name = input('Please enter User name: ')
    age = int(input('Please enter User age: '))
    status = bool(input('Please enter User status: '))

    dict_entry = {'id': id, 'name': name, 'age': age, 'status': status}
    users_list.append(dict_entry)
    print(f'User {name} was successfully added!')
    pass


def option2():
    print('--------------------------------------------')
    print(users_list)
    print('--------------------------------------------')
    pass


def option3():
    print('--------------------------------------------')
    print(sorted(users_list, key=lambda x: x['age']))
    print('--------------------------------------------')
    pass


def option4():
    id_user = input('Please provide User Id you want to delete: ')
    for i in range(len(users_list)):
        if users_list[i]['id'] == id_user:
            del users_list[i]
            break

def option5():
    id_user_2 = int(input('Please provide User Id you want to change Status: '))
    for user in range(len(users_list)):
        if users_list[user]['id'] == id_user_2:
            if not users_list[user]['status']:
                users_list[user]['status'] = True
            else:
                users_list[user]['status'] = False
    pass


while True:
    print_menu()
    print('--------------------------------------------')
    option = int(input('Your choice: '))

    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        option5()
    elif option == 6:
        print('Program has finished. Goodbye!')
        exit()
    else:
        print('--------------------------------------------')
        print('Please select your option from 1 to 6.')
        print('--------------------------------------------')
