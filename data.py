# Тела POST-запросов.

# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
URL_SERVICE             = "https://40df7b2e-8a47-4abc-aebe-fd4d846541fd.serverhub.praktikum-services.ru"
URL_CREATE_ORDERS_PATH  = "/api/v1/orders"
URL_TRACK               = "/v1/orders/track?t="

track       = "000000"

headers = {"Content-Type": "application/json"}

# Данные заказа. Для создания новой записи заказа в системе.
orders_body = {
    "firstName": "Сергей",                  # - Имя клиента
    "lastName": "Абдурахмангаджи",                 # - Фамилия клиента
    "address": "169710",                    # - Адрес доставки
    "metroStation": "40",                   # - Номер станции метро
    "phone": "+34916123451",                # - Телефон
    "rentTime": 5,                          # - На сколько дней аренда самоката
    "deliveryDate": "2024-10-07",           # - Дата аренды
    "comment": "Привет, Абдурахмангаджи!",  # - Комментарии
    "color": ["BLACK", "GREY"]              # - Цвета самоката, подходящие клиенту.
    }

track_1 = 0
