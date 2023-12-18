from loopring.session import Session
import requests
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class OrderAmounts:
    minimum: str
    maximum: str
    dust: str


@dataclass
class GasAmounts:
    distribution: str
    deposit: str


@dataclass
class TokenInfo:
    type: str
    tokenId: int
    symbol: str
    name: str
    address: str
    decimals: int
    precision: int
    precisionForOrder: int
    orderAmounts: OrderAmounts
    luckyTokenAmounts: OrderAmounts
    fastWithdrawLimit: str
    gasAmounts: GasAmounts
    enabled: bool


@dataclass
class OnchainFee:
    type: str
    fee: str


@dataclass
class ExchangeInfo:
    chainId: int
    exchangeAddress: str
    depositAddress: str
    onchainFees: List[OnchainFee]
    openAccountFees: List[dict]
    updateFees: List[dict]
    transferFees: List[dict]
    withdrawalFees: List[dict]
    fastWithdrawalFees: List[dict]
    ammExitFees: List[dict]


@dataclass
class MarketInfo:
    market: str
    baseTokenId: int
    quoteTokenId: int
    precisionForPrice: int
    orderbookAggLevels: int
    enabled: bool


class Exchange(Session):

    def get_tokens(self) -> list[TokenInfo]:
        """
        Get the tokens supported by the Loopring protocol.

        :return: List of tokens.
        """
        url = f'{self.base_url}/exchange/tokens'

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return [TokenInfo(**entry) for entry in data]
        else:
            print("Error fetching tokens:", response.status_code)
            return response.json()

    def get_exchange_info(self) -> ExchangeInfo:
        """
        Get the exchange info.

        :return: Exchange Info.
        """
        url = f'{self.base_url}/exchange/info'

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return ExchangeInfo(**data)
        else:
            print("Error fetching tokens:", response.status_code)
            return response.json()

    def get_markets(self) -> list[MarketInfo]:
        """
        Get the markets supported by the Loopring protocol.

        :return: List of markets.
        """
        url = f'{self.base_url}/exchange/markets'

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return [MarketInfo(**entry) for entry in data['markets']]
        else:
            print("Error fetching markets:", response.status_code)
            return response.json()

