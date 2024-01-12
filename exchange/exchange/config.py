from local_config import PHONE_NUMBER, EMAIL_ADDRESS


rules = {
    'archive': False,
    'email': {
        'receiver': EMAIL_ADDRESS,
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
