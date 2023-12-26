from dotenv import load_dotenv
import os


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
    def initialize(cls):
        """
        Initialize the Loopring API with API key and account ID.
        """
        load_dotenv()
        cls.api_key = os.environ.get("API_KEY")
        cls.account_id = os.environ.get("ACCOUNT_ID")
        cls.headers = {
            'Accept': 'application/json',
            'X-API-KEY': cls.api_key
        }
