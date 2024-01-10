from local_config import API_KEY
BASE_PATH = 'http://data.fixer.io/api/latest?access_key='


url = BASE_PATH+API_KEY

rules = {
    'archive': True,
    'send_mail': True,
    # 'preferred': None
    'preferred': ['IRR', 'USD', 'BTC']
}

RECEIVER_EMAIL = 'mehranredrose@gmail.com'
