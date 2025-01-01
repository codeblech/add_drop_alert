### What
Alert for the time when the add-drop elective option is opened up on the JIIT WebPortal

### Why
So, we can drop our shitty electives as fast as possible.

### Steps to recreate
1. Follow the steps [here](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started) and create all the meta and FaceBook accounts needed to interact with WhatsApp programatically.
2. Follow the [above link](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started) and create "A business app", add the Recipient Phone Number, and add templates.
3. Fork and Clone this repo.
4. Create a `.env` file in ROOT of this project.
5. Set the following keys in the `.env` file:
```
JIIT_USERNAME="xxx"
JIIT_PASSWORD="xxx"
WHATSAPP_ACCESS_TOKEN="xxx"
PHONE_NUMBER="xxx"
```
6. Also set these keys and values in the Repository secrets for your forked repository. Make sure to use exact names at both places.
7. Modify the `.github/workflows/add_drop_alert.yaml` according to your needs. By default, alerts are sent every 30 minutes.


### Note
This project uses a slightly modified version of [pyjiit](https://github.com/codelif/pyjiit)

The `pyjiit.wrapper.WebPortal.__hit()` method is modified to not raise an error on the failure response by the server. Failure response implies add drop option is not available.


### Future
Email and Telegram alerts.
