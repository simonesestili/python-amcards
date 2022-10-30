from datetime import datetime

REQUIRED_SHIPPING_ADDRESS_FIELDS = {
    'first_name',
    'last_name',
    'address_line_1',
    'city',
    'state',
    'postal_code',
    'country',
}

OPTIONAL_SHIPPING_ADDRESS_FIELDS = {
    'organization',
    'third_party_contact_id',
}

OPTIONAL_RETURN_ADDRESS_FIELDS = {
    'first_name',
    'last_name',
    'address_line_1',
    'city',
    'state',
    'postal_code',
    'country',
}

def to_datetime(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f') 

def format_cents(price_in_cents: int) -> str:
    whole, fractional = map(str, divmod(price_in_cents, 100))
    fractional = fractional.zfill(2)
    return f'${whole}.{fractional}'

def get_missing_required_shipping_address_fields(shipping_address: dict) -> list:
    missings = []
    for req in REQUIRED_SHIPPING_ADDRESS_FIELDS:
        if shipping_address.get(req, '').strip(): continue
        missings.append(req)
    return missings

def is_valid_date(date: str) -> bool:
    if not isinstance(date, str): return False
    if len(date) != 10: return False
    if date.count('-') != 2 or date[4] != '-' or date[7] != '-': return False
    for part in date.split('-'):
        if not part.isdigit():
            return False
    return True

def sanitize_shipping_address(shipping_address: dict) -> dict:
    sanitized_shipping_address = {field: shipping_address[field] for field in shipping_address}
    for optional in OPTIONAL_SHIPPING_ADDRESS_FIELDS:
        if optional not in shipping_address: continue
        sanitized_shipping_address[optional] = shipping_address[optional]
    return sanitized_shipping_address

def sanitize_return_address(return_address: dict) -> dict:
    sanitized_return_address = {}
    for optional in OPTIONAL_RETURN_ADDRESS_FIELDS:
        if optional not in return_address: continue
        sanitized_return_address[optional] = return_address[optional]
    return sanitized_return_address
