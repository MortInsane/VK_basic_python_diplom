from vk import VK
from ya_disk import YandexDisk
import os

TOKEN = ...
Yandex_TOKEN = ...
username = ...

files_path = os.path.join(os.getcwd(), 'files')

v = VK(token=TOKEN, user=username, version="5.131")
v.collection_data()

ya = YandexDisk(token=Yandex_TOKEN, json_path=files_path, user_folder=username)
ya.upload()
