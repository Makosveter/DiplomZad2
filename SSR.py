import requests

import data


# 1)
# Определение для отправки POST-запроса на создание заказа на самокат.
def post_new_orders(body):
    return requests.post(data.URL_SERVICE + data.URL_CREATE_ORDERS_PATH,
                         json = body,
                         headers = data.headers)

# 2)
# Определение для отправки POST-запроса на создание заказа на самокат.
def get_orders(track):
    return requests.get(data.URL_SERVICE + data.URL_TRACK,track)

# 3)
# Функция для позитивной проверки
def new_track(body):
    resp = post_new_orders(body)
    return resp;

# 4)
# Функция для позитивной проверки
def positive_assert():
    # В переменную kits_body сохраняется ответ на запрос
    get_orders_response = get_orders(data.track_1)

    # Проверяется, что код ответа равен 200
    assert get_orders_response.status_code == 200
