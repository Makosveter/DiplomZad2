# Тела POST-запросов.

# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
import configuration

headers = {
    "Content-Type": "application/json"
    }

# Данные пользователя. Для создания новой записи пользователя в системе.
user_body = {
    "firstName": "Анатолий",  # Имя пользователя
    "phone": "+79995553322",  # Контактный телефон пользователя
    "address": "г. Москва, ул. Пушкина, д. 10"  # Адрес пользователя
    }

kit_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer f6f5f89f-e7f2-4f81-ac96-bff37b6f796c"
    }

kit_body = {
    "name": "Новый набор"
    }

