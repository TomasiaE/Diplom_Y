
import configuration
import requests

#Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_AN_ORDER,
                         json=body)


#Получение заказа по его номеру
def get_an_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_AN_ORDER + str(track))

