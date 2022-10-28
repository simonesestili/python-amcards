from datetime import datetime


from . import __helpers as helpers


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        credits: int,
        date_joined: datetime,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        domestic_postage_cost: int,
        international_postage_cost: int,
        domestic_postage_countries: set,
        greeting_card_cost: int,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.credits = credits
        self.date_joined = date_joined
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.domestic_postage_cost = domestic_postage_cost
        self.international_postage_cost = international_postage_cost
        self.domestic_postage_countries = domestic_postage_countries
        self.greeting_card_cost = greeting_card_cost

    def __repr__(self) -> str:
        return (
            '('
            f'first_name={self.first_name}, '
            f'last_name={self.last_name}, '
            f'credits={self.credits}, '
            f'date_joined={self.date_joined}, '
            f'street={self.street}, '
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
            f'Street: {self.street}\n'
            f'City: {self.city}\n'
            f'State: {self.state}\n'
            f'Postal Code: {self.postal_code}\n'
            f'Country: {self.country}\n'
            f'Domestic Postage Cost: {formatted_domestic_postage_cost}\n'
            f'International Postage Cost: {formatted_international_postage_cost}\n'
            f'Domestic Postage Countries: {formatted_domestic_postage_countries}\n'
            f'Greeting Card Cost: {formatted_greeting_card_cost}\n'
        )