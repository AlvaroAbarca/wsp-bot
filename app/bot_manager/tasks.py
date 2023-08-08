from celery import shared_task

import requests
import json

from django.utils import timezone
from users.models import Person

@shared_task
def send_message_id(chat_id: str, message: str):

    url = "http://openwa:8080/sendText"
    payload = json.dumps({
        "args": {
            "to": chat_id,
            "content": message
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload, verify=False)
    print(chat_id)
    print(message)
    print(response.json())


@shared_task
def check_birthdays(chat_id: str, initial_msg: str|None) -> None:
    today = timezone.localdate(timezone.now())

    users = Person.objects.filter(birthday__month=today.month, birthday__day=today.day)

    msg = "Feliz Cumpleanos: \n"
    for user in users:
        msg += f"- {user.name} {user.last_name}\n"

    if users.exists():
        print("Encontre usuarios")
        send_message_id(chat_id="56945378118@c.us", message=msg)
    else:
        print("No encontre usuarios")

