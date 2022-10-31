from typing import List
from datetime import datetime


from . import __helpers as helpers


class User:
    """.. _amcards.models.User:

    Represents an AMcards user.

    """
    def __init__(
        self,
        first_name: str,
        last_name: str,
        credits: int,
        date_joined: datetime,
        address_line_1: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        domestic_postage_cost: int,
        international_postage_cost: int,
        domestic_postage_countries: set,
        greeting_card_cost: int,
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._credits = credits
        self._date_joined = date_joined
        self._address_line_1 = address_line_1
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._country = country
        self._domestic_postage_cost = domestic_postage_cost
        self._international_postage_cost = international_postage_cost
        self._domestic_postage_countries = domestic_postage_countries
        self._greeting_card_cost = greeting_card_cost

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def credits(self) -> int:
        return self._credits

    @property
    def date_joined(self) -> datetime:
        return self._date_joined

    @property
    def address_line_1(self) -> str:
        return self._address_line_1

    @property
    def city(self) -> str:
        return self._city

    @property
    def state(self) -> str:
        return self._state

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @property
    def country(self) -> str:
        return self._country

    @property
    def domestic_postage_cost(self) -> int:
        return self._domestic_postage_cost

    @property
    def international_postage_cost(self) -> int:
        return self._international_postage_cost

    @property
    def domestic_postage_countries(self) -> set:
        return self._domestic_postage_countries

    @property
    def greeting_card_cost(self) -> int:
        return self._greeting_card_cost

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            first_name=json['first_name'],
            last_name=json['last_name'],
            credits=json['credits'],
            date_joined=helpers.to_datetime(json['date_joined']),
            address_line_1=json['address_line_1'],
            city=json['city'],
            state=json['state'],
            postal_code=json['postal'],
            country=json['country'],
            domestic_postage_cost=json['postage']['domestic_cost'],
            international_postage_cost=json['postage']['international_cost'],
            domestic_postage_countries=set(json['postage']['domestic_countries']),
            greeting_card_cost=json['product_pricing_info']['5x7greetingcard']
        )

    def __repr__(self) -> str:
        return (
            '('
            f'first_name={self.first_name}, '
            f'last_name={self.last_name}, '
            f'credits={self.credits}, '
            f'date_joined={self.date_joined}, '
            f'address_line_1={self.address_line_1}, '
            f'city={self.city}, '
            f'state={self.state}, '
            f'postal_code={self.postal_code}, '
            f'country={self.country}, '
            f'domestic_postage_cost={self.domestic_postage_cost}, '
            f'international_postage_cost={self.international_postage_cost}, '
            f'domestic_postage_countries={self.domestic_postage_countries}, '
            f'greeting_card_cost={self.greeting_card_cost}'
            ')'
        )

    def __str__(self) -> str:
        formatted_credits = helpers.format_cents(price_in_cents=self.credits)
        formatted_domestic_postage_cost = helpers.format_cents(price_in_cents=self.domestic_postage_cost)
        formatted_international_postage_cost = helpers.format_cents(price_in_cents=self.international_postage_cost)
        formatted_greeting_card_cost = helpers.format_cents(price_in_cents=self.greeting_card_cost)
        formatted_domestic_postage_countries = ', '.join(self.domestic_postage_countries)
        return (
            f'First Name: {self.first_name}\n'
            f'Last Name: {self.last_name}\n'
            f'Credit Balance: {formatted_credits}\n'
            f'Date Joined: {self.date_joined}\n'
            f'Address Line 1: {self.address_line_1}\n'
            f'City: {self.city}\n'
            f'State: {self.state}\n'
            f'Postal Code: {self.postal_code}\n'
            f'Country: {self.country}\n'
            f'Domestic Postage Cost: {formatted_domestic_postage_cost}\n'
            f'International Postage Cost: {formatted_international_postage_cost}\n'
            f'Domestic Postage Countries: {formatted_domestic_postage_countries}\n'
            f'Greeting Card Cost: {formatted_greeting_card_cost}\n'
        )

class Gift:
    """.. _amcards.models.Gift:

    Represents an AMcards gift.

    """
    def __init__(
        self,
        name: str,
        thumbnail: str,
        base_cost: int,
        shipping_and_handling_cost: int,
    ) -> None:
        self._name = name
        self._thumbnail = thumbnail
        self._base_cost = base_cost
        self._shipping_and_handling_cost = shipping_and_handling_cost

    @property
    def name(self) -> str:
        return self._name

    @property
    def thumbnail(self) -> str:
        return self._thumbnail

    @property
    def base_cost(self) -> int:
        return self._base_cost

    @property
    def shipping_and_handling_cost(self) -> int:
        return self._shipping_and_handling_cost

    @property
    def total_cost(self) -> int:
        return self._base_cost + self._shipping_and_handling_cost

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            name=json['gift_name'],
            thumbnail=json['image'],
            base_cost=json['price'],
            shipping_and_handling_cost=json['shipping_and_handling'],
        )

    def __repr__(self) -> str:
        return (
            '('
            f'name={self.name}, '
            f'thumbnail={self.thumbnail}, '
            f'cost={self.cost}, '
            f'shipping_and_handling_cost={self.shipping_and_handling_cost}'
            ')'
        )

class Template:
    """.. _amcards.models.Template:

    Represents an AMcards template.

    """
    def __init__(
        self,
        id: int,
        name: str,
        thumbnail: str,
        gifts: List[Gift],
    ) -> None:
        self._id = id
        self._name = name
        self._thumbnail = thumbnail
        self._gifts = gifts

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def thumbnail(self) -> str:
        return self._thumbnail

    @property
    def gifts(self) -> List[Gift]:
        return self._gifts

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            id=json['id'],
            name=json['name'],
            thumbnail=json['thumbnail'],
            gifts=[Gift._from_json(gift_json) for gift_json in json['gifts']],
        )

    def __repr__(self) -> str:
        return (
            '('
            f'id={self.id}, '
            f'name={self.name}, '
            f'thumbnail={self.thumbnail}, '
            f'gifts={self.gifts}'
            ')'
        )

class Campaign:
    """.. _amcards.models.Campaign:

    Represents an AMcards drip campaign.

    """
    def __init__(
        self,
        id: int,
        name: str,
        send_if_duplicate: bool = False,
    ) -> None:
        self._id = id
        self._name = name
        self._send_if_duplicate = send_if_duplicate

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def send_if_duplicate(self) -> bool:
        return self._send_if_duplicate

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            id=json['id'],
            name=json['title'],
            send_if_duplicate=json['send_even_if_duplicate'],
        )

    def __repr__(self) -> str:
        return (
            '('
            f'id={self.id}, '
            f'name={self.name}, '
            f'send_if_duplicate={self.send_if_duplicate}'
            ')'
        )

class CardResponse:
    """.. _amcards.models.CardResponse:

    Represents AMcards' response for sending a single card.

    """
    def __init__(
        self,
        card_id: int,
        total_cost: int,
        user_email: str,
    ) -> None:
        self._card_id = card_id
        self._total_cost = total_cost
        self._user_email = user_email

    @property
    def card_id(self) -> int:
        return self._card_id

    @property
    def total_cost(self) -> int:
        return self._total_cost

    @property
    def user_email(self) -> str:
        return self._user_email

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            card_id=json['card'],
            total_cost=json['total_cost'],
            user_email=json['user'],
        )

class CampaignResponse:
    """.. _amcards.models.CampaignResponse:

    Represents AMcards' response for sending a single drip campaign.

    """
    def __init__(
        self,
        mailing_id: int,
        card_ids: List[int],
        user_email: str,
    ) -> None:
        self._mailing_id = mailing_id
        self._card_ids = card_ids
        self._user_email = user_email

    @property
    def mailing_id(self) -> int:
        return self._mailing_id

    @property
    def card_ids(self) -> List[int]:
        return self._card_ids

    @property
    def user_email(self) -> str:
        return self._user_email

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            mailing_id=json['mailing'],
            card_ids=json['cards'],
            user_email=json['user'],
        )
