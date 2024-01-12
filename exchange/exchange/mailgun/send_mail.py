import json
from mail import send_api_mail
from config import rules
from jalali_time import jalali


def send_mail(timestamp, rates):
    """
    get timestamp and rates if there is any preferred rates send them to the entered emails
    """
    subject = f'{timestamp} - {jalali} - rates'
    if rules['email']['preferred'] is not None:
        tmp = {}
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
    rates = tmp
    text = json.dumps(rates)

    send_api_mail(subject, text)
