import requests

orderID = 7
url = 'https://petstore.swagger.io/v2/store/order/'
headers = {'accept': 'application/json', 'ContentType': 'application/json'}

# POST - запрос. Оформление заказа.
data = {
  "id": orderID,
  "petId": 1110,
  "quantity": 10,
  "shipDate": "2023-06-27T18:43:44.951Z",
  "status": "placed",
  "complete": True
}
res = requests.post(f"{url}", json=data, headers=headers)
print()
print('Оформление заказа. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# GET - запрос. Найти заказ по id.
res = requests.get(f"{url}+{orderID}", headers=headers)
print('Найти заказ по id. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# DELETE - запрос. Удалить заказ по id.
res = requests.delete(f"{url}+{orderID}", headers=headers)
print('Удалить заказ по id. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
print('-'*150)
print()

# GET - запрос. Возвращает сопоставление кодов состояния с количествами
res = requests.get(f"https://petstore.swagger.io/v2/store/inventory", headers=headers)
print('Возвращает сопоставление кодов состояния с количествами. Статус код:', res.status_code)
print(res.json())
print('Тип данных:', type(res.json()))
