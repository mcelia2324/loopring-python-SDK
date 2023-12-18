from loopring.session import Session
import requests
from dataclasses import dataclass
from typing import Optional


@dataclass
class PendingTransactions:
    """
    Dataclass for pending transactions.
    """
    withdraw: str
    deposit: str


@dataclass
class Balance:
    """
    Dataclass for account balances.
    """
    accountId: int
    tokenId: int
    total: str
    locked: str
    pending: PendingTransactions


class Account(Session):

    def get_account_balances(
        self,
        address: str = "",
        tokens: str = ""
    ) -> list[Balance]:
        """
        Get the balances for the account associated with the API key.

        :param address: Address of the account to fetch balances for.
        :param tokens: List of token IDs to fetch balances for.

        :return: Dataclass.
        """
        url = (f'{self.base_url}/user/balances?accountId={self.account_id}'
               f'&address={address}&tokens={tokens}')

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return [Balance(**entry) for entry in data]
        else:
            print("Error fetching account balance:", response.status_code)
            return response.json()

