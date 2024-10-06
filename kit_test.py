import requests

import data
import sender_stand_request

# Создание пользователя
User1 = sender_stand_request.post_new_user(data.user_body)

# Сохраняем токин
token = User1.json()["authToken"]


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_01_create_kit():
    sender_stand_request.positive_assert('а', token)

# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_02_create_kit():
    sender_stand_request.positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC', token)

# Тест 3. Негативное создание набора. Параметр name состоит символов меньше допустимого 0
def test_03_create_kit():
    sender_stand_request.negative_assert('', token)

# Тест 4. Негативное создание набора. Параметр name состоит символов больше допустимого 512
def test_04_create_kit():
    sender_stand_request.negative_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD', token)

# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_05_create_kit():
    sender_stand_request.positive_assert('Мария', token)

# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_06_create_kit():
    sender_stand_request.positive_assert('Мария', token)

# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_07_create_kit():
    sender_stand_request.positive_assert('№%@,', token)

# Тест 8. Успешное создание набора. Параметр name содержит пробелы
def test_08_create_kit():
    sender_stand_request.positive_assert('Человек и КО', token)

# Тест 9. Успешное создание набора. Параметр name состоит из цифр
def test_09_create_kit():
    sender_stand_request.positive_assert('123', token)

# Тест 10. Негативное создание набора. Параметр name не передан в заросе.
def test_10_create_kit():
    sender_stand_request.negative_assert_2(token)

# Тест 11. Негативное создание набора. Параметр name состоит символов цифр
def test_11_create_kit():
    sender_stand_request.negative_assert('123', token)