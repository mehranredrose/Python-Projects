from local_config import API_KEY
BASE_PATH = 'http://data.fixer.io/api/latest?access_key='


url = BASE_PATH+API_KEY

rules = {
    'archive': True,
    'email': {
        'receiver': 'mehranredrose@gmail.com',
        'enable': True,
        # 'preferred': None
        'preferred': ['IRR', 'USD', 'BTC']
    },
    'notification': {
        'enable': True,
        'receiver': '09123456789',
        'preferred': {'IRR': {min: '45000', max: ''}, 'USD': {min: ':1.090000', max: ':1.095000'}}
    }
}
