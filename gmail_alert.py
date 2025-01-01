import os
from dotenv import load_dotenv
import yagmail
from portal import Status, get_add_drop_endpoint_status
from pprint import pprint

# load_dotenv()

from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")


def send_email(status: Status):
    yag = yagmail.SMTP(from_email, oauth2_file="~/oauth2_creds.json")
    # contents = [
    #     "This is the body, and here is just text http://somedomain/image.png",
    #     "You can find an audio file attached.",
    #     "/local/path/song.mp3",
    # ]
    if status == Status.OPEN:
        contents = ["Add Drop is now Open."]
    elif status == Status.CLOSED:
        contents = ["Add Drop is still Closed"]
    else:
        raise ValueError(
            f"Invalid status: {status}. Expected Status.OPEN or Status.CLOSED."
        )
    yag.send(subject=contents, contents=contents)


def main():
    pprint("start")
    add_drop_status = get_add_drop_endpoint_status()
    if add_drop_status == "Failure":
        pprint("sending add drop closed email")
        send_email(status=Status.CLOSED)
    else:
        pprint("sending add drop open email")
        send_email(status=Status.OPEN)
    pprint("email sent")


if __name__ == "__main__":
    main()
