from datetime import datetime


def to_datetime(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f') 

def format_cents(price_in_cents: int) -> str:
    whole, fractional = map(str, divmod(price_in_cents, 100))
    fractional = fractional.zfill(2)
    return f'${whole}.{fractional}'