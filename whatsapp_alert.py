from portal import get_add_drop_endpoint_status, Status
import requests
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

phone_number = os.getenv("PHONE_NUMBER")

closed_payload = {
    "messaging_product": "whatsapp",
    "to": phone_number,
    "type": "template",
    "template": {
        "namespace": "cfc2b7b0_627c_4b43_ad0a_fa24d6117735",
        "name": "add_drop_closed",
        "language": {"code": "en"},
    },
}

open_payload = {
    "messaging_product": "whatsapp",
    "to": phone_number,
    "type": "template",
    "template": {
        "namespace": "cfc2b7b0_627c_4b43_ad0a_fa24d6117735",
        "name": "add_drop_open_now",
        "language": {"code": "en"},
    },
}

default_template = {
    "messaging_product": "whatsapp",
    "to": phone_number,
    "type": "template",
    "template": {"name": "hello_world", "language": {"code": "en_US"}},
}


def send_whatsapp_message(status: Status):
    headers = {
        "Authorization": f"Bearer {os.getenv('WHATSAPP_ACCESS_TOKEN')}",
        "Content-Type": "application/json",
    }
    if status == Status.OPEN:
        payload = open_payload
    elif status == Status.CLOSED:
        payload = closed_payload
    else:
        raise ValueError(
            f"Invalid status: {status}. Expected Status.OPEN or Status.CLOSED."
        )

    response = requests.post(
        "https://graph.facebook.com/v21.0/489410244263052/messages",
        headers=headers,
        json=payload,
    )
    pprint("Response from Whatsapp API:")
    pprint(response.text)


def main():
    add_drop_status = get_add_drop_endpoint_status()
    if add_drop_status == "Failure":
        send_whatsapp_message(status=Status.CLOSED)
    else:
        send_whatsapp_message(status=Status.OPEN)


if __name__ == "__main__":
    main()
