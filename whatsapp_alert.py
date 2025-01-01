from portal import get_add_drop_endpoint_status, Status
import requests
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

closed_template_name = "add_drop_closed"
opened_template_name = "add_drop_open_now"

closed_payload = {
    "messaging_product": "whatsapp",
    "to": "919997703037",
    "type": "template",
    "template": {"name": closed_template_name, "language": {"code": "en_US"}},
}

open_payload = {
    "messaging_product": "whatsapp",
    "to": "919997703037",
    "type": "template",
    "template": {"name": opened_template_name, "language": {"code": "en_US"}},
}

default_template = {
    "messaging_product": "whatsapp",
    "to": "919997703037",
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
        payload - closed_payload
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
