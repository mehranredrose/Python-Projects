import requests
import json
from config import url, rules
from mail import send_api_mail


def get_rates():
    """
        send a get request to fixer.io api and get live rates
        :return: request.response instance
    """
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    """
    gets filename and rates and save them to a specific directory
    """
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    """
    get timestamp and rates if there is any preferred rates send them to the entered emails
    """
    subject = f'{timestamp} rates'
    if rules['email']['preferred'] is not None:
        tmp = {}
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
    rates = tmp
    text = json.dumps(rates)

    send_api_mail(subject, text)


def check_notify_rules(rates):
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred:
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reaced min : {rates[exc]}'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reaced max : {rates[exc]}'

    return msg


def send_notification():
    pass


if __name__ == "__main__":
    response = get_rates()
    if rules['archive']:
        archive(response['timestamp'], response['rates'])
    if rules['email']['enable']:
        send_mail(response['timestamp'], response['rates'])
    if rules['notification']['enable']:
        check_notify_rules(response['rates'])
        send_notification()
