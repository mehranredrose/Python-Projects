import requests
import json
BASE_PATH = 'http://data.fixer.io/api/latest?access_key='


def get_rates(api_key):
    """
        send a get request to fixer.io api and get live rates
        :return: request.response instance
    """
    response = requests.get(BASE_PATH+api_key)
    if response.status_code == 200:
        return json.loads(response.text)

    return None
