from typing import List
from loopring.account import Balance
from loopring.exchange import TokenInfo
from dataclasses import dataclass
from typing import Dict


@dataclass
class DetailedBalance:
    """
    A dataclass that combines the Balance and TokenInfo dataclasses.

    converted_total is the total amount in regular units (e.g. 1.0 ETH).
    """
    accountId: int
    tokenId: int
    total: str
    converted_total: float
    locked: str
    pending: Dict[str, str]
    symbol: str
    name: str
    address: str
    decimals: int


def convert_from_wei(amount: str, decimals: int) -> float:
    """
    Convert an amount from wei (or similar smallest unit) to a regular unit.

    :param amount: The amount in the smallest unit (as a string to avoid floating point issues).
    :param decimals: The number of decimal places to shift.
    :return: The amount in regular units as a float.
    """
    amount_in_wei = int(amount)
    return amount_in_wei / (10 ** decimals)


def join_balance_with_token_info(
    balances: List[Balance],
    tokens: List[TokenInfo]
) -> list[DetailedBalance]:
    """
    Join the Balance dataclass with the TokenInfo dataclass.
    """
    token_info_map = {token.tokenId: token for token in tokens}
    joined_data = []
    for balance in balances:
        token_info = token_info_map.get(balance.tokenId)
        if token_info:
            combined_data = {
                'accountId': balance.accountId,
                'tokenId': balance.tokenId,
                'total': balance.total,
                'converted_total': convert_from_wei(balance.total, token_info.decimals),
                'locked': balance.locked,
                'pending': balance.pending,
                'symbol': token_info.symbol,
                'name': token_info.name,
                'address': token_info.address,
                'decimals': token_info.decimals

            }
            joined_data.append(combined_data)

    return [DetailedBalance(**entry) for entry in joined_data]

