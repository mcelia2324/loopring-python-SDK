

class Session:
    """
    Parent class for Loopring API.
    """
    # Class variables
    api_key = None
    account_id = None
    headers = None
    base_url = 'https://api3.loopring.io/api/v3'

    @classmethod
    def initialize(cls, api_key: str, account_id: str):
        """
        Initialize the Loopring API with API key and account ID.

        :param api_key: API key for Loopring.
        :param account_id: Account ID for Loopring.
        """
        cls.api_key = api_key
        cls.account_id = account_id
        cls.headers = {
            'Accept': 'application/json',
            'X-API-KEY': api_key
        }
