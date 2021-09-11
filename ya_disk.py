import requests


class YandexDisk:
    def __init__(self, token, json_file):
        self.token = token
        self.json_file = json_file

    def get_url_to_download(self):
        params = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}",
            "path": "VK_"
        }




