import requests
import json

url = 'https://petstore.swagger.io/v2/user/'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

# POST - запрос. Создание списка пользователей с заданым входным массивом.
data = [
    {
        "id": 1,
        "username": "Sasha_M",
        "firstName": "Sasha",
        "lastName": "M",
        "email": "1@nm.ru",
        "password": "12",
        "phone": "12313",
        "userStatus": 10
    },
    {
        "id": 2,
        "username": "Mish_Sa",
        "firstName": "Misha",
        "lastName": "Samuilov",
        "email": "2@nm.ru",
        "password": "1245",
        "phone": "6731223",
        "userStatus": 11
    },
    {
        "id": 3,
        "username": "C_K",
        "firstName": "Tosha",
        "lastName": "K",
        "email": "3@nm.ru",
        "password": "127345",
        "phone": "127223",
        "userStatus": 12
    }
]
createWithArray = 'createWithArray'
res = requests.post(f"{url}{createWithArray}", json=data, headers=headers)
print()
print('Создание списка пользователей с заданым входным массивом. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-' * 150)
print()

# GET - запрос. Получаем данные о пользователи, используя его username.
username = 'Sasha_M'
res = requests.get(f"{url}{username}", headers=headers)
print('Получаем данные о пользователи, используя его username. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# Далее все запросы выполняются с этим username
username = 'Sasha_M'

# PUT - запрос. Изменяем данные пользователя по username.
data = {
        "id": 1,
        "username": "Sasha_M",
        "firstName": "S",
        "lastName": "",
        "email": "56@nm.ru",
        "password": "12",
        "phone": "",
        "userStatus": 10
    }
res = requests.put(f"{url}{username}", json=data, headers=headers)
print('Изменяем данные пользователя по username. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# GET - запрос. Получаем данные о пользователи, используя его username.
res = requests.get(f"{url}{username}", headers=headers)
print('Получаем данные о пользователи, используя его username. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# GET - запрос. Получаем логи пользователя.
password = '12'
username = 'Sasha_M'
res = requests.get(f"{url}login?username={username}&password={password}", headers=headers, data=data)
print('Получаем логи пользователя. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# GET - запрос. Выход из текущего сеанса пользователя.
res = requests.get(f"{url}logout", headers=headers)
print('Выход из текущего сеанса пользователя. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()


# DELETE - запрос. Удалить пользователя по username.
res = requests.delete(f"{url}{username}", headers=headers)
print('Удалить пользователя по username. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()
