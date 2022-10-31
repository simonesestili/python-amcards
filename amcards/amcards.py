import requests
from typing import List


from .models import User, Template, Gift, Campaign, CardResponse, CampaignResponse
from . import exceptions
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

        return User._from_json(user_json)

    def templates(self) -> List[Template]:
        res = requests.get(url=f'{DOMAIN}/.api/v1/template/', headers=self.HEADERS)
        templates_json = res.json().get('objects', [])

        if not templates_json:
            return None

        return [Template._from_json(template_json) for template_json in templates_json]

    def quicksends(self) -> List[Template]:
        res = requests.get(url=f'{DOMAIN}/.api/v1/quicksendtemplate/', headers=self.HEADERS)
        templates_json = res.json().get('objects', [])

        if not templates_json:
            return None

        return [Template._from_json(template_json) for template_json in templates_json]

    def campaigns(self) -> List[Campaign]:
        res = requests.get(url=f'{DOMAIN}/.api/v1/campaign/', headers=self.HEADERS)
        campaigns_json = res.json().get('objects', [])

        if not campaigns_json:
            return None

        return [Campaign._from_json(campaign_json) for campaign_json in campaigns_json]

    def send_card(
        self,
        template_id: str | int,
        initiator: str,
        shipping_address: dict,
        return_address: dict = None,
        send_date: str = None
    ):
        # Validate shipping address
        missings = helpers.get_missing_required_shipping_address_fields(shipping_address)
        if missings:
            error_message = 'Missing the following required shipping address fields: ' + ', '.join(missings)
            raise exceptions.ShippingAddressError(error_message)

        # Validate send date
        if send_date is not None and not helpers.is_valid_date(send_date):
            error_message = 'Invalid send_date format, please specify date as "YYYY-MM-DD", or omit it'
            raise exceptions.DateFormatError(error_message)

        # Sanitize shipping address and return address
        shipping_address = helpers.sanitize_shipping_address_for_card_send(shipping_address)
        if return_address is not None:
            return_address = helpers.sanitize_return_address(return_address)
            # prefix return address fields with return_
            return_address = {f'return_{key}': value for key, value in return_address.items()}

        # Build request json payload
        body = {
            'template_id': template_id,
            'initiator': initiator,
        } | shipping_address

        if return_address is not None:
            body |= return_address

        if send_date is not None:
            body |= {'send_date': send_date}

        res = requests.post(f'{DOMAIN}/cards/open-card-form-oa/', json=body, headers=self.HEADERS)

        # Check for errors
        match res.status_code:
            case 401:
                raise exceptions.AuthenticationError('Access token provided to client is unauthorized')
            case 402:
                raise exceptions.InsufficientCreditsError('Clients\' user has insufficient credits, no card was scheduled')
            case 403:
                raise exceptions.ForbiddenTemplateError(f'Clients\' user does not own given template with id of {template_id}')

        res_json = res.json()
        return CardResponse._from_json(res_json)

    def send_campaign(
        self,
        campaign_id: str | int,
        initiator: str,
        shipping_address: dict,
        return_address: dict = None,
        send_date: str = None
    ):
        # Validate shipping address
        missings = helpers.get_missing_required_shipping_address_fields(shipping_address)
        if missings:
            error_message = 'Missing the following required shipping address fields: ' + ', '.join(missings)
            raise exceptions.ShippingAddressError(error_message)

        # Validate send date
        if send_date is not None and not helpers.is_valid_date(send_date):
            error_message = 'Invalid send_date format, please specify date as "YYYY-MM-DD", or omit it'
            raise exceptions.DateFormatError(error_message)

        # Sanitize shipping address and return address
        shipping_address = helpers.sanitize_shipping_address_for_campaign_send(shipping_address)
        if return_address is not None:
            return_address = helpers.sanitize_return_address(return_address)
            # prefix return address fields with return_
            return_address = {f'return_{key}': value for key, value in return_address.items()}

        # Validate birth_date
        if 'birth_date' in shipping_address and not helpers.is_valid_date(shipping_address['birth_date']):
            error_message = 'Invalid birth_date format, please specify date as "YYYY-MM-DD", or omit it'
            raise exceptions.DateFormatError(error_message)
        # Validate anniversary_date
        if 'anniversary_date' in shipping_address and not helpers.is_valid_date(shipping_address['anniversary_date']):
            error_message = 'Invalid anniversary_date format, please specify date as "YYYY-MM-DD", or omit it'
            raise exceptions.DateFormatError(error_message)
        # Validate phone_number
        if 'phone_number' in shipping_address and not helpers.is_valid_phone(shipping_address['phone_number']):
            error_message = 'Invalid phone_number format, please specify phone as a 10 number string with no special formatting (ex. 15556667777), or omit it'
            raise exceptions.PhoneFormatError(error_message)

        # Build request json payload
        body = {
            'campaign_id': campaign_id,
            'initiator': initiator,
        } | shipping_address

        if return_address is not None:
            body |= return_address

        if send_date is not None:
            body |= {'send_date': send_date}

        res = requests.post(f'{DOMAIN}/campaigns/open-campaign-form/', json=body, headers=self.HEADERS)

        # Check for errors
        match res.status_code:
            case 401:
                raise exceptions.AuthenticationError('Access token provided to client is unauthorized')
            case 402:
                raise exceptions.InsufficientCreditsError('Clients\' user has insufficient credits, no cards were scheduled')
            case 403:
                raise exceptions.ForbiddenCampaignError(f'Clients\' user does not own given campaign with id of {campaign_id}')
            case 409:
                raise exceptions.DuplicateCampaignError('Duplicates were detected, no cards were scheduled')

        res_json = res.json()
        return CampaignResponse._from_json(res_json)
