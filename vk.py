from datetime import datetime
import requests
import json


TOKEN = ""
username = ""


class VK:
    def __init__(self, token, version, user):
        self.token = token
        self.version = version
        self.user = user

    def _get_id_by_username(self):
        data = {}
        params = {
            "user_ids": self.user,
            "access_token": self.token,
            "v": self.version
        }

        url = f"https://api.vk.com/method/users.get"
        response = requests.get(url, params=params).json()

        for item in response['response']:
            user_id = item['id']
            first_name = item['first_name']
            last_name = item['last_name']

            data[user_id] = {"first_name": first_name, "last_name": last_name}
        return data

    def collection_data(self):
        data = {}
        users_data = self._get_id_by_username()

        for user_id, user_data in users_data.items():

            params = {
                "album_id": "profile",
                "extended": 1,
                "access_token": self.token,
                "v": self.version,
                "owner_id": user_id
            }

            url = f"https://api.vk.com/method/photos.get"
            response = requests.get(url, params=params, timeout=5).json()
            base_json = response['response']['items']

            for item in base_json:
                likes = item['likes']['count']
                sizes = item['sizes']
                photo_type = sizes[-1]['type']
                max_size_url = sizes[-1]['url']

                str_date = item['date']
                str_date = datetime.fromtimestamp(str_date).strftime("%d-%m-%Y_%H%M%S")

                if user_id not in data:
                    data[user_id] = {}

                if f"{likes}.jpg" not in data[user_id]:

                    data[user_id][f"{likes}.jpg"] = {"photo_type": photo_type, "photo_url": max_size_url}
                else:
                    data[user_id][f"{likes}_{str_date}.jpg"] = {"photo_type": photo_type, "photo_url": max_size_url}

            with open(f'{self.user}-{user_id}_result.json', 'w') as f:
                json.dump(data, f, indent=2)
