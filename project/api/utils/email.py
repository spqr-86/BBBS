from typing import List

import requests
from os import getenv


def send_email(to_email: List, subject: str, text: str):
    return requests.post(
        getenv('MAIL_API'),
        auth=("api", getenv('MAIL_API_KEY')),
        data={
            "from": getenv('FROM_MAIL'),
            "to": [to_email],
            "subject": subject,
            "text": text
        })
