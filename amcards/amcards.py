import requests


from .models import User
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

        return User(
            first_name=user_json['first_name'],
            last_name=user_json['last_name'],
            credits=user_json['credits'],
            date_joined=helpers.to_datetime(user_json['date_joined']),
            street=user_json['address_line_1'],
            city=user_json['city'],
            state=user_json['state'],
            postal_code=user_json['postal'],
            country=user_json['country'],
            domestic_postage_cost=user_json['postage']['domestic_cost'],
            international_postage_cost=user_json['postage']['international_cost'],
            domestic_postage_countries=set(user_json['postage']['domestic_countries']),
            greeting_card_cost=user_json['product_pricing_info']['5x7greetingcard']
        )
