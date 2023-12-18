from loopring.session import Session
import requests
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class OffchainRequestType(Enum):
    ORDER = '0'
    OFFCHAIN_WITHDRAWAL = '1'
    UPDATE_ACCOUNT = '2'
    TRANSFER = '3'
    FAST_OFFCHAIN_WITHDRAWAL = '4'
    OPEN_ACCOUNT = '5'
    AMM_EXIT = '6'
    DEPOSIT = '7'
    AMM_JOIN = '8'
    NFT_MINT = '9'
    NFT_WITHDRAWAL = '10'
    NFT_TRANSFER = '11'
    DEPLOY_TOKENADDRESS = '13'
    TRANSFER_AND_UPDATE_ACCOUNT = '15'
    NFT_TRANSFER_AND_UPDATE_ACCOUNT = '19'


@dataclass
class FeeItem:
    token: str
    tokenId: int
    fee: str
    discount: float


@dataclass
class FeesData:
    gasPrice: str
    fees: List[FeeItem]


@dataclass
class OrderInfo:
    minAmount: str
    makerRate: int
    takerRate: int


@dataclass
class AmountInfo:
    tokenSymbol: str
    baseOrderInfo: OrderInfo
    userOrderInfo: OrderInfo
    tradeCost: str


@dataclass
class TradeData:
    gasPrice: str
    amounts: List[AmountInfo]
    cacheOverdueAt: int


@dataclass
class MarketOrderDetails:
    minimum: str
    maximum: str
    dust: str


@dataclass
class NFTAmountDetails:
    feeTokenSymbol: str
    minAmount: str
    tradeCost: str
    marketOrderInfo: MarketOrderDetails


@dataclass
class NFTTradeInfo:
    nftTokenAddress: str
    feeRate: int
    amounts: List[NFTAmountDetails]
    gasPrice: str
    cacheOverdueAt: int


class Fees(Session):

    def get_erc20_offchain_fees(
        self,
        request_type: OffchainRequestType,
        token: str = str(),
        amount: str = str()
    ) -> FeesData:
        """
        Get the ERC20 fees for the account associated with the API key.

        :param request_type: OffchainRequestType
        :param token: str (e.g. 'ETH')
        :param amount:

        :return: Dataclass.
        """
        url = (f'{self.base_url}/user/offchainFee?accountId={self.account_id}&requestType={request_type.value}'
               f'&tokenSymbol={token}&amount={amount}')

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return FeesData(**data)
        else:
            print("Error fetching account balance:", response.status_code)
            return response.json()

    def get_erc20_order_fees(self, market: str) -> TradeData:
        """
        Get the ERC20 Order fees for the account associated with the API key.

        :param market: str (e.g. 'LRC-ETH')

        :return: Dataclass.
        """
        url = f'{self.base_url}/user/orderUserRateAmount?accountId={self.account_id}&market={market}'

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return TradeData(**data)
        else:
            print("Error fetching account balance:", response.status_code)
            return response.json()

    def get_nft_offchain_fees(
        self,
        request_type: OffchainRequestType,
        token_address: str = str(),
        deploy_in_withdraw: str = "false"
    ) -> FeesData:
        """
        Get the ERC20 Offchain NFT fees for the account associated with the API key.

        :param request_type: OffchainRequestType
        :param token_address: str (e.g. 'ETH')
        :param deploy_in_withdraw:

        :return: Dataclass.
        """
        url = (f'{self.base_url}/user/nft/offchainFee?accountId={self.account_id}&requestType={request_type.value}'
               f'&tokenAddress={token_address}&deployInWithdraw={deploy_in_withdraw}')

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return FeesData(**data)
        else:
            print("Error fetching account balance:", response.status_code)
            return response.json()

    def get_nft_order_fees(
        self,
        nft_token_address: str,
        fee_token_symbol: str
    ) -> NFTTradeInfo:
        """
        Get the ERC20 NFT Order fees for the account associated with the API key.

        :param fee_token_symbol:
        :param nft_token_address: str (e.g. 'ETH')

        :return: Dataclass.
        """
        url = (f'{self.base_url}/nft/info/orderUserRateAmount?accountId={self.account_id}'
               f'&nftTokenAddress={nft_token_address}&feeTokenSymbol={fee_token_symbol}')

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return NFTTradeInfo(**data)
        else:
            print("Error fetching account balance:", response.status_code)
            return response.json()
