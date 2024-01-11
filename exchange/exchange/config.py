from local_config import API_KEY, PHONE_NUMBER
BASE_PATH = 'http://data.fixer.io/api/latest?access_key='


url = BASE_PATH+API_KEY

rules = {
    'archive': False,
    'email': {
        'receiver': 'mehranredrose@gmail.com',
        'enable': False,
        # 'preferred': None
        'preferred': ['IRR', 'USD', 'BTC']
    },
    'notification': {
        'enable': True,
        'receiver': PHONE_NUMBER,
        'preferred': {'IRR': {min: '45000', max: '45900'}, 'USD': {min: ':1.090000', max: ':1.095000'}}
    }
}
