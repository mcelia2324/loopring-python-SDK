import pickle
from loopring.session import Session
from loopring.account import Account
from loopring.exchange import Exchange
from utils import join_balance_with_token_info


# Initialize the Loopring API with API key and account ID
Session.initialize()

# Get the account balances
account = Account()
balances = account.get_account_balances()

# Get token info on exchange
exchange = Exchange()
tokens = exchange.get_tokens()

# Combines the two dataclasses objects (balances and tokens) into one
# Doing so allows you to see things like the token symbol and name
join = join_balance_with_token_info(balances, tokens)
for i in join:
    print(i)
