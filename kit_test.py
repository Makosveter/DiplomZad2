
import data

import SSR


# Создание карточки заказа.
body_1 = data.orders_body

# Создание переменной track_1.
#orders_1 #= SSR.post_new_orders(body_1)
#track_1 = 0
# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа


# def test_give_others_track():
#     orders_1 = SSR.post_new_orders(body_1)
#     data.track_1 = orders_1.json()['track']
#
#
# def test_get_reqest_orders():
#     SSR.get_orders(data.track_1)
#
#
# def test_get_other_response():
#     SSR.positive_assert()

def test_Alesya():
    # 1.1 Выполнить запрос на создание  заказа.
    body = data.orders_body
    orders = SSR.post_new_orders(body)
    # 1.2 Сохранить номер трека заказа.
    track = orders.json()["track"]
    # 2.1 Выполнить запрос на получения заказа по треку заказа.
    get_orders_response =SSR.get_orders(track)
    # 2.2 Проверить, что код ответа равен 200.
    assert get_orders_response.status_code == 200

