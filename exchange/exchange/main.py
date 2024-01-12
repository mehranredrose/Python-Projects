import json

from config import rules
from local_config import API_KEY
from notification import send_sms
from jalali_time import jalali

from fixer import get_rates
from mailgun import send_mail


def archive(filename, rates):
    """
    gets filename and rates and save them to a specific directory
    """
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def check_notify_rules(rates):
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred:
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reaced min : {rates[exc]}'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reaced max : {rates[exc]}'

    return msg


def send_notification(msg):
    msg = msg + '/n' + jalali
    send_sms(msg)


if __name__ == "__main__":
    response = get_rates(API_KEY)
    if rules['archive']:
        archive(response['timestamp'], response['rates'])
    if rules['email']['enable']:
        send_mail(response['timestamp'], response['rates'])
    if rules['notification']['enable']:
        notification_msg = check_notify_rules(response['rates'])
        if notification_msg:
            print(notification_msg)
            send_notification(notification_msg)
