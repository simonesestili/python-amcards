class AMcardsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ShippingAddressError(AMcardsException, ValueError):
    """Some shipping address fields are missing or invalid"""

class AuthenticationError(AMcardsException):
    """Access token provided to client is unauthorized"""

class InsufficientCreditsError(AMcardsException):
    """Clients' user has insufficient credits"""

class DateFormatError(AMcardsException, ValueError):
    """Invalid format for send date"""