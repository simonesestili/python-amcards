from enum import Enum
from datetime import datetime
from typing import List, Optional


from . import __helpers as helpers


class User:
    """Represents an AMcards user."""
    def __init__(
        self,
        id: int,
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
        self._id = id
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

    __repr__ = helpers.repr

    @property
    def id(self) -> int:
        """User's unique identifier."""
        return self._id

    @property
    def first_name(self) -> str:
        """User's first name."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """User's last name."""
        return self._last_name

    @property
    def credits(self) -> int:
        """User's credit balance in `cents`."""
        return self._credits

    @property
    def date_joined(self) -> datetime:
        """Date and time when user created their AMcards account."""
        return self._date_joined

    @property
    def address_line_1(self) -> str:
        """User's primary address line (street)."""
        """Primary address line of user."""
        return self._address_line_1

    @property
    def city(self) -> str:
        """User's state."""
        return self._city

    @property
    def state(self) -> str:
        """User's state/province."""
        return self._state

    @property
    def postal_code(self) -> str:
        """User's postal code"""
        return self._postal_code

    @property
    def country(self) -> str:
        """User's country."""
        return self._country

    @property
    def domestic_postage_cost(self) -> int:
        """User's postage cost for sending cards to countries in :py:attr:`domestic_postage_countries`."""
        return self._domestic_postage_cost

    @property
    def international_postage_cost(self) -> int:
        """User's postage cost for sending cards to countries not in :py:attr:`domestic_postage_countries`."""
        return self._international_postage_cost

    @property
    def domestic_postage_countries(self) -> set:
        """User's countries that have a :py:attr:`domestic_postage_cost`."""
        return self._domestic_postage_countries

    @property
    def greeting_card_cost(self) -> int:
        """User's base cost of a greeting card excluding postage."""
        return self._greeting_card_cost

    @classmethod
    def _from_json(cls, json: dict):
        user_id = json['resource_uri']
        user_id = user_id[user_id.find('user/')+5:]
        if not user_id[-1].isdigit(): user_id = user_id[:-1]
        return cls(
            id=int(user_id),
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

class Gift:
    """Represents an AMcards gift."""
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

    __repr__ = helpers.repr

    @property
    def name(self) -> str:
        """Gift's name."""
        return self._name

    @property
    def thumbnail(self) -> str:
        """Gift's image thumbnail."""
        return self._thumbnail

    @property
    def base_cost(self) -> int:
        """Gift's base cost in `cents`."""
        return self._base_cost

    @property
    def shipping_and_handling_cost(self) -> int:
        """Gift's shipping and handling cost in `cents`."""
        return self._shipping_and_handling_cost

    @property
    def total_cost(self) -> int:
        """Gift's total cost, including :py:attr:`base_cost` + :py:attr:`shipping_and_handling_cost` in `cents`."""
        return self._base_cost + self._shipping_and_handling_cost

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            name=json['gift_name'],
            thumbnail=json['image'],
            base_cost=json['price'],
            shipping_and_handling_cost=json['shipping_and_handling'],
        )

class Template:
    """Represents an AMcards template."""
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
        self._gifts_total = sum(gift.total_cost for gift in gifts)

    __repr__ = helpers.repr

    @property
    def id(self) -> int:
        """Template's unique identifier."""
        return self._id

    @property
    def name(self) -> str:
        """Template's name."""
        return self._name

    @property
    def thumbnail(self) -> str:
        """Template's image thumbnail."""
        return self._thumbnail

    @property
    def gifts(self) -> List[Gift]:
        """List of template's :py:class:`gifts <amcards.models.Gift>` (could be an empty list)."""
        return self._gifts

    @property
    def gifts_total(self) -> int:
        """Sum of gifts' total costs in `cents`."""
        return self._gifts_total

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            id=json['id'],
            name=json['name'],
            thumbnail=json['thumbnail'],
            gifts=[Gift._from_json(gift_json) for gift_json in json['gifts']],
        )

class Campaign:
    """Represents an AMcards drip campaign."""
    def __init__(
        self,
        id: int,
        name: str,
        send_if_duplicate: bool,
    ) -> None:
        self._id = id
        self._name = name
        self._send_if_duplicate = send_if_duplicate

    __repr__ = helpers.repr

    @property
    def id(self) -> int:
        """Drip campaign's unique identifier."""
        return self._id

    @property
    def name(self) -> str:
        """Drip campaign's name."""
        return self._name

    @property
    def send_if_duplicate(self) -> bool:
        """If True, AMcards will not attempt to detect and prevent duplicates. Otherwise, if this campaign has been previously sent to a contact, further campaign send attempts to the same contact will be prevented."""
        return self._send_if_duplicate

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            id=json['id'],
            name=json['title'],
            send_if_duplicate=json['send_even_if_duplicate'],
        )

class CardStatus(Enum):
    """Represents the status of an AMcards card."""
    EDITABLE = 0
    VERIFYING_ADDRESS = 1
    IN_THE_MAIL = 2
    FLAGGED = 3
    DELIVERED = 4
    READY_FOR_PRINT = 5
    PRINTED = 6
    PROCESSING = 7
    REFUNDED = 8
    TESTING = 9

class Card:
    """Represents an AMcards card."""
    def __init__(
        self,
        id: int,
        amount_charged: int,
        status: CardStatus,
        initiator: str,
        send_date: str,
        date_created: datetime,
        date_last_modified: datetime,
        date_fulfilled: datetime,
        is_international: bool,
        campaign_id: Optional[int],
        shipping_address: dict,
        return_address: dict,
    ) -> None:
        self._id = id
        self._amount_charged = amount_charged
        self._status = status
        self._initiator = initiator
        self._send_date = send_date
        self._date_created = date_created
        self._date_last_modified = date_last_modified
        self._date_fulfilled = date_fulfilled
        self._is_international = is_international
        self._campaign_id = campaign_id
        self._shipping_address = shipping_address
        self._return_address = return_address

    __repr__ = helpers.repr

    @property
    def id(self) -> int:
        """Card's unique identifier."""
        return self._id

    @property
    def amount_charged(self) -> int:
        """Total amount charged to client's user in `cents`."""
        return self._amount_charged

    @property
    def status(self) -> CardStatus:
        """Current status of card."""
        return self._status

    @property
    def initiator(self) -> str:
        """Unique identifier of client's user so if multiple users use a single AMcards.com account, a card can be identified per person."""
        return self._initiator

    @property
    def send_date(self) -> str:
        """The date the card is sent. If not specified, the card is scheduled for the day after it was created and the value will be ``None``. The format should be: ``"YYYY-MM-DD"``."""
        return self._send_date

    @property
    def date_created(self) -> datetime:
        """Date and time card was created."""
        return self._date_created

    @property
    def date_last_modified(self) -> Optional[datetime]:
        """Date and time card was last modified. ``None`` if not modified yet."""
        return self._date_last_modified

    @property
    def date_fulfilled(self) -> Optional[datetime]:
        """Date and time card was fulfilled. ``None`` if not fulfilled yet."""
        return self._date_fulfilled

    @property
    def is_international(self) -> bool:
        """If True, card was shipped international. If False, card was shipped domestic."""
        return self._is_international

    @property
    def campaign_id(self) -> Optional[int]:
        """Unique identifier for drip campaign associated with this card. If this card is not a part of a drip campaign, this value will be ``None``."""
        return self._campaign_id

    @property
    def shipping_address(self) -> dict:
        """Shipping address for the card.
        In the form:

            .. code-block::

                {
                    'first_name': 'Ralph',
                    'last_name': 'Mullins',
                    'address_line_1': '2285 Reppert Road',
                    'city': 'Southfield',
                    'state': 'MI',
                    'postal_code': '48075',
                    'country': 'US',
                    'organization': 'Google',                # OPTIONAL
                    'third_party_contact_id': 'crmid1453131' # OPTIONAL
                }

        """
        return self._shipping_address

    @property
    def return_address(self) -> dict:
        """Return address for the card.
        In the form:

            .. code-block::

                {
                    'first_name': 'Ralph',                   # OPTIONAL
                    'last_name': 'Mullins',                  # OPTIONAL
                    'address_line_1': '2285 Reppert Road',   # OPTIONAL
                    'city': 'Southfield',                    # OPTIONAL
                    'state': 'MI',                           # OPTIONAL
                    'postal_code': '48075',                  # OPTIONAL
                    'country': 'US',                         # OPTIONAL
                }

        """
        return self._return_address

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            id=json['id'],
            amount_charged=int(json['amount_charged'] * 100),
            status=CardStatus(json['status']),
            initiator=json['initiator'],
            send_date=json['send_date'],
            date_created=helpers.to_datetime(json['created']),
            date_last_modified=helpers.to_datetime(json['last_modified']),
            date_fulfilled=helpers.to_datetime(json['fulfilled']),
            is_international=json['is_international'],
            campaign_id=json['campaign_pk'],
            shipping_address=helpers.parse_shipping_address(json),
            return_address=helpers.parse_return_address(json),
        )

class MailingStatus(Enum):
    """Represents the status of an AMcards mailing."""
    COMPLETE = 0
    PROCESSING = 1

class Mailing:
    """Represents an AMcards mailing."""
    def __init__(
        self,
        id: int,
        amount_charged: int,
        cards: List[Card],
        status: MailingStatus,
        date_created: datetime,
    ) -> None:
        self._id = id
        self._amount_charged = amount_charged
        self._cards = cards
        self._status = status
        self._date_created = date_created

    __repr__ = helpers.repr

    @property
    def id(self) -> int:
        """Mailing's unique identifier."""
        return self._id

    @property
    def amount_charged(self) -> int:
        """Total amount charged to client's user in `cents`."""
        return self._amount_charged

    @property
    def cards(self) -> List[Card]:
        """All cards that are a part of this mailing."""
        return self._cards

    @property
    def status(self) -> MailingStatus:
        """Current status of mailing."""
        return self._status

    @property
    def date_created(self) -> datetime:
        """Date and time mailing was created."""
        return self._date_created

    # @classmethod
    # def _from_json(cls, json: dict):
    #     recipients = json['report']['recipients']
    #     return cls(
    #         id=json['id'],
    #         amount_charged=int(json['amount_charged']),
    #         status=CardStatus(json['status']),
    #         date_created=helpers.to_datetime(json['created']),
    #     )

class Contact:
    """Represents an AMcards contact."""
    def __init__(
        self,
        id: int,
        date_created: datetime,
        date_last_modified: Optional[datetime],
        date_last_card_send: Optional[datetime],
        notes: Optional[str],
        email: Optional[str],
        first_name: str,
        last_name: str,
        address_line_1: str,
        city: str,
        state: str,
        postal_code: str,
        country: Optional[str],
        organization: Optional[str],
        phone: Optional[str],
        birth_year: Optional[str],
        birth_month: Optional[str],
        birth_day: Optional[str],
        anniversary_year: Optional[str],
        anniversary_month: Optional[str],
        anniversary_day: Optional[str],
    ) -> None:
        self._id = id
        self._date_created = date_created
        self._date_last_modified = date_last_modified
        self._date_last_card_send = date_last_card_send
        self._notes = notes
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._address_line_1 = address_line_1
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._country = country
        self._organization = organization
        self._phone = phone
        self._birth_year = birth_year
        self._birth_month = birth_month
        self._birth_day = birth_day
        self._anniversary_year = anniversary_year
        self._anniversary_month = anniversary_month
        self._anniversary_day = anniversary_day

    __repr__ = helpers.repr

    @property
    def id(self) -> int:
        """Contact's unique identifier."""
        return self._id

    @property
    def date_created(self) -> datetime:
        """Date and time contact was created."""
        return self._date_created

    @property
    def date_last_modified(self) -> Optional[datetime]:
        """Date and time contact was last modified. ``None`` if never modified."""
        return self._date_last_modified

    @property
    def date_last_card_send(self) -> Optional[datetime]:
        """Date and time card was last sent to contact. ``None`` if card has never been sent to this contact."""
        return self._date_last_card_send

    @property
    def notes(self) -> Optional[str]:
        """Contact's notes. ``None`` if contact has no notes."""
        return self._notes

    @property
    def email(self) -> Optional[str]:
        """Contact's email address. ``None`` if contact doesn't have an email address."""
        return self._email

    @property
    def first_name(self) -> str:
        """Contact's first name."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """Contact's last name."""
        return self._last_name

    @property
    def address_line_1(self) -> str:
        """Contact's primary address line."""
        return self._address_line_1

    @property
    def city(self) -> str:
        """Contact's city."""
        return self._city

    @property
    def state(self) -> str:
        """Contact's state/province."""
        return self._state

    @property
    def postal_code(self) -> str:
        """Contact's postal code."""
        return self._postal_code

    @property
    def country(self) -> Optional[str]:
        """Contact's country. ``None`` if contact doesn't have a country."""
        return self._country

    @property
    def organization(self) -> Optional[str]:
        """Contact's organization/company. ``None`` if contact doesn't have an organization."""
        return self._organization

    @property
    def phone(self) -> Optional[str]:
        """Contact's phone number. ``None`` if contact doesn't have a phone number."""
        return self._phone

    @property
    def birth_year(self) -> Optional[str]:
        """Contact's birth year in the form ``"YYYY"``. ``None`` if contact doesn't have a birth year."""
        return self._birth_year

    @property
    def birth_month(self) -> Optional[str]:
        """Contact's birth month in the form ``"MM"``. ``None`` if contact doesn't have a birth month."""
        return self._birth_month

    @property
    def birth_day(self) -> Optional[str]:
        """Contact's birth day in the form ``"DD"``. ``None`` if contact doesn't have a birth day."""
        return self._birth_day

    @property
    def anniversary_year(self) -> Optional[str]:
        """Contact's anniversary year in the form ``"YYYY"``. ``None`` if contact doesn't have an anniversary year."""
        return self._anniversary_year

    @property
    def anniversary_month(self) -> Optional[str]:
        """Contact's anniversary month in the form ``"MM"``. ``None`` if contact doesn't have an anniversary month."""
        return self._anniversary_month

    @property
    def anniversary_day(self) -> Optional[str]:
        """Contact's anniversary day in the form ``"DD"``. ``None`` if contact doesn't have an anniversary day."""
        return self._anniversary_day

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            id=int(json['id']),
            date_created=helpers.to_datetime(json['added']),
            date_last_modified=helpers.to_datetime(json['updated']),
            date_last_card_send=helpers.to_datetime(json['last_card_send_date']),
            notes=json['notes'] if json['notes'] else None,
            email=json['email_address'] if json['email_address'] else None,
            first_name=json['first_name'],
            last_name=json['last_name'],
            address_line_1=json['address_line_1'],
            city=json['city'],
            state=json['state'],
            postal_code=json['postal_code'],
            country=json['country'] if json['country'] else None,
            organization=json['organization'] if json['organization'] else None,
            phone=json['phone_number'] if json['phone_number'] else None,
            birth_year=json['birth_year'] if json['birth_year'] else None,
            birth_month=json['birth_month'] if json['birth_month'] else None,
            birth_day=json['birth_day'] if json['birth_day'] else None,
            anniversary_year=json['anniversary_year'] if json['anniversary_year'] else None,
            anniversary_month=json['anniversary_month'] if json['anniversary_month'] else None,
            anniversary_day=json['anniversary_day'] if json['anniversary_day'] else None,
        )

class CardResponse:
    """Represents AMcards' response for sending a single card."""
    def __init__(
        self,
        card_id: int,
        total_cost: int,
        user_email: str,
        message: str,
        shipping_address: dict,
    ) -> None:
        self._card_id = card_id
        self._total_cost = total_cost
        self._user_email = user_email
        self._message = message
        self._shipping_address = shipping_address

    __repr__ = helpers.repr

    @property
    def card_id(self) -> int:
        """Unique id for the :py:class:`card <amcards.models.Card>` created."""
        return self._card_id

    @property
    def total_cost(self) -> int:
        """Total cost the client's user was charged in `cents`."""
        return self._total_cost

    @property
    def user_email(self) -> str:
        """Client's user email."""
        return self._user_email

    @property
    def message(self) -> str:
        """AMcards' response message for sending a single card."""
        return self._message

    @property
    def shipping_address(self) -> dict:
        """Shipping address for this CardResponse."""
        return self._shipping_address

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            card_id=json['card'],
            total_cost=json['total_cost'],
            user_email=json['user'],
            message=json['message'],
            shipping_address=json['shipping_address'],
        )

class CampaignResponse:
    """Represents AMcards' response for sending a single drip campaign."""
    def __init__(
        self,
        mailing_id: int,
        card_ids: List[int],
        user_email: str,
        message: str,
        shipping_address: dict,
    ) -> None:
        self._mailing_id = mailing_id
        self._card_ids = card_ids
        self._user_email = user_email
        self._message = message
        self._shipping_address = shipping_address

    __repr__ = helpers.repr

    @property
    def mailing_id(self) -> int:
        """Unique id for the :py:class:`mailing <amcards.models.Mailing>` created."""
        return self._mailing_id

    @property
    def card_ids(self) -> List[int]:
        """List of unique ids for the :py:class:`cards <amcards.models.Card>` created."""
        return self._card_ids

    @property
    def user_email(self) -> str:
        """Client's user email."""
        return self._user_email

    @property
    def message(self) -> str:
        """Represents AMcards' response message for sending a single drip campaign."""
        return self._message

    @property
    def shipping_address(self) -> dict:
        """Shipping address for this CampaignResponse."""
        return self._shipping_address

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            mailing_id=json['mailing'],
            card_ids=json['cards'],
            user_email=json['user'],
            message=json['message'],
            shipping_address=json['shipping_address'],
        )

class CardsResponse:
    """Represents AMcards' response for sending multiple cards."""
    def __init__(
        self,
        mailing_id: int,
        user_email: str,
        message: str,
        shipping_addresses: List[dict],
    ) -> None:
        self._mailing_id = mailing_id
        self._user_email = user_email
        self._message = message
        self._shipping_addresses = shipping_addresses

    __repr__ = helpers.repr

    @property
    def mailing_id(self) -> int:
        """Unique id for the :py:class:`mailing <amcards.models.Mailing>` created."""
        return self._mailing_id

    @property
    def user_email(self) -> str:
        """Client's user email."""
        return self._user_email

    @property
    def message(self) -> str:
        """AMcards' response message for sending multiple cards."""
        return self._message

    @property
    def shipping_addresses(self) -> List[dict]:
        """Shipping addresses for this CardsResponse."""
        return self._shipping_addresses

    @classmethod
    def _from_json(cls, json: dict):
        return cls(
            mailing_id=int(json['mailing_uri'][17:-1]),
            user_email=json['user'],
            message=json['message'],
            shipping_addresses=json['shipping_addresses'],
        )