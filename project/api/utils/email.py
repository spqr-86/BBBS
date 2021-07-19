import requests
from typing import List

from django.conf import settings


def send_email(to_email: List, subject: str, text: str):
    return requests.post(
        settings.MAIL_API,
        auth=('api', settings.MAIL_API_KEY),
        data={
            'from': settings.FROM_MAIL,
            'to': [to_email],
            'subject': subject,
            'text': text,
        },
    )
