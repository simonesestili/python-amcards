import requests
from typing import List


from .models import User, Template, Gift, Campaign
from . import __helpers as helpers


DOMAIN = 'https://amcards.com'


class AMcardsClient:
    def __init__(self, access_token: str) -> None:
        self._access_token = access_token
        self.HEADERS = {
            'Authorization': f'Bearer {access_token}',
        }

    def user(self) -> User:
        res = requests.get(url=f'{DOMAIN}/.api/v1/user/', headers=self.HEADERS)
        user_json = res.json().get('objects', [{}])[0]

        if not user_json:
            return None

        return User.from_json(user_json)

    def templates(self) -> List[Template]:
        res = requests.get(url=f'{DOMAIN}/.api/v1/template/', headers=self.HEADERS)
        templates_json = res.json().get('objects', [])

        if not templates_json:
            return None

        return list(map(Template.from_json, templates_json))

    def quicksends(self) -> List[Template]:
        res = requests.get(url=f'{DOMAIN}/.api/v1/quicksendtemplate/', headers=self.HEADERS)
        templates_json = res.json().get('objects', [])

        if not templates_json:
            return None

        return list(map(Template.from_json, templates_json))

    def campaigns(self) -> List[Campaign]:
        res = requests.get(url=f'{DOMAIN}/.api/v1/campaign/', headers=self.HEADERS)
        campaigns_json = res.json().get('objects', [])

        if not campaigns_json:
            return None

        return list(map(Campaign.from_json, campaigns_json))

