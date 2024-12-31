from pyjiit.wrapper import Webportal
from pyjiit.wrapper import API
from pyjiit.default import CAPTCHA
import os
from dotenv import load_dotenv

load_dotenv()


def main():

    ENDPOINT = "/addDropSubjectRequest/getStudentInfo"

    w = Webportal()
    USERNAME = os.getenv("LOGIN_USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    print(USERNAME)
    print(PASSWORD)

    w.student_login(USERNAME, PASSWORD, CAPTCHA)
    PAYLOAD = {
        "instituteid": "11IN1902J000001",
        "bypassValue": "XuVHxhCQsRmMyK7cUdFClQ==",
    }
    resp = w._Webportal__hit("POST", API + ENDPOINT, json=PAYLOAD, authenticated=True)
    print(resp["status"]["responseStatus"])


if __name__ == "__main__":
    main()
