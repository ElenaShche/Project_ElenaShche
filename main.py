
# Щекина Елена -  6 когорта, финальный проект. Инженер по тестированию плюс.
import config
import requests
import data
def post_new_order(): #создание нового заказа
    return requests.post(config.URL+config.CREATE_ORDER,
                         json=data.order_body)
res=post_new_order()
number=res.json()['track'] #сохранение номера заказа
#print(number)
def get_oder_id(): #получение заказа по его номеру
    return requests.get(config.URL+config.GET_ORDER,
                        params={"t":number})
ord=get_oder_id()
#print(ord.json())
assert ord.status_code==200 #проверка, что код ответа равен 200
