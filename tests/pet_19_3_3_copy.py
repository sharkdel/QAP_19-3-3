import requests

petId = 11
url = 'https://petstore.swagger.io/v2/pet/'
headers = {'accept': 'application/json', 'ContentType': 'application/json'}

# POST - запрос. Добавляем питомца.
data = {
  "id": petId,
  "category": {
    "id": 12450,
    "name": "cat"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 2460,
      "name": "cat_main"
    }
  ],
  "status": "available"
}

res = requests.post(f"{url}", json=data, headers=headers)
print()
print('Добавляем питомца. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# PUT - запрос. Изменяем данные питомца.
data = {
  "id": petId,
  "category": {
    "id": 55550,
    "name": "cat"
  },
  "name": "cat_tail",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 60,
      "name": "kitty"
    }
  ],
  "status": "available"
}
#data.update(name='Squirrel', status='pending')
res = requests.put(f"{url}", json=data, headers=headers)
print('Изменяем данные питомца. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# POST - запрос. Обновление данных питомца в магазине с помощью формы.
res = requests.post(f"{url}+{petId}", data={"name": "Ground", "status": "pending"},
                    headers={'accept': 'application/json', 'ContentType': 'application/x-www-form-urlencoded'})
print('Обновление данных питомца в магазине с помощью формы. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# POST - запрос. Добавляем фото питомца.
#file1 = dict(file=open('images/5657675.jpg', 'rb'))
res = requests.post(f"{url}+{petId}/uploadImage", headers={'accept': 'application/json'},
                    files={'file': ('image.jpg', open('images/5657675.jpg', 'rb'), 'image/jpeg')})
print('Добавляем фото питомца. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# GET - запрос. Смотрим данные питомца.
res = requests.get(f"{url}+{petId}", json=data, headers=headers)
print('Смотрим данные питомца. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# DELETE - запрос. Удаляем питомца.
#res = requests.delete(f"{url}+{petId}", headers=headers)
#print('Удаляем питомца. Статус код:', res.status_code)
#print(res.json())
#print('Тип данных:', type(res.json()))
