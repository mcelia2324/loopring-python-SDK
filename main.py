import pickle
from loopring.session import Session
from loopring.account import Account
from loopring.exchange import Exchange
from utils import join_balance_with_token_info

# Set your API key and account ID
creds = {'api_key': 'YOUR_API_KEY', 'account_id': 'YOUR_ACCOUNT_ID'}

# Save your creds to a serialized pickle file
with open('loopringCreds.pickle', 'wb') as f:
    pickle.dump(creds, f)


# Load the creds file and set the API key and account ID
with open('loopringCreds.pickle', 'rb') as f:
    creds = pickle.load(f)
    api_key = creds['api_key']
    account_id = creds['account_id']

# Initialize the Loopring API with API key and account ID
Session.initialize(api_key, account_id)

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
