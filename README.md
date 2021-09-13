# Парсинг фотографий из профиля(только аватарки) VK и загрузка на Yandex Disk

Парсинг осуществляется на основе общедоступных данных
Для запуска необходимо получить 2 токена доступа

## Получение vk токена(ключ доступа пользователя)
[Ссылка](https://vk.com/dev/implicit_flow_user) на получение токена vk

## Получение yandex токена
[Ссылка](https://yandex.ru/dev/disk/poligon/) на получение токена yandex

В файле main.py отредактировать следующие строки
```python
VK_TOKEN = ...
Yandex_TOKEN = ...
username = ...
```
Атрибут **count_to_upload** экземпляра класса **VK**, задает количество загружаемых файлов

Запустить main.py

В Яндекс диске создается папка VK далее подпапка с именем
"user.name-фамилия имя-id", внутрь которой загружаются фото из вк.