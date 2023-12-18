import pickle
from loopring.session import Session
from loopring.account import Account
from loopring.exchange import Exchange
from loopring.fees import Fees, OffchainRequestType

"""
# Set your API key and account ID
creds = {'api_key': 'YOUR_API_KEY', 'account_id': 'YOUR_ACCOUNT_ID'}

# Save your creds to a serialized pickle file
with open('loopringCreds.pickle', 'wb') as f:
    pickle.dump(creds, f)
"""


# Load the creds file and set the API key and account ID
with open('loopringCreds.pickle', 'rb') as f:
    creds = pickle.load(f)
    api_key = creds['api_key']
    account_id = creds['account_id']

# Initialize the Loopring API with API key and account ID
loopring = Session.initialize(api_key, account_id)

# Get the account balances
account = Account()
balances = account.get_account_balances()
print(balances)

# Get token info on exchange
exchange = Exchange()
tokens = exchange.get_markets()
for i in tokens:
    print(i)

fee = Fees()
fees = fee.get_erc20_offchain_fees(OffchainRequestType.UPDATE_ACCOUNT)
print(fees)

