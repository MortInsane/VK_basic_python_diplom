from datetime import datetime
import requests
import json


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
            first_name = user_data["first_name"]
            last_name = user_data["last_name"]

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

                data.setdefault("results", dict())
                data["id"] = user_id
                data["first_name"] = first_name
                data["last_name"] = last_name
                data["user_name"] = self.user

                if f"{likes}.jpg" not in data["results"]:

                    data["results"][f"{likes}.jpg"] = {"photo_type": photo_type, "photo_url": max_size_url}
                else:
                    data["results"][f"{likes}_{str_date}.jpg"] = {"photo_type": photo_type, "photo_url": max_size_url}

            with open(f'files/{self.user}-{first_name} {last_name}-{user_id}.json', 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
