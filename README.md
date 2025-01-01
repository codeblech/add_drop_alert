## What
Alert for the time when the add-drop elective option is opened up on the JIIT WebPortal

## Why
So, we can drop our shitty electives as fast as possible.

## Steps to recreate

### Telegram
Telegram is GOAT.

1. Fork this repo
2. Follow the instructions [here](https://v2.openhab.org/addons/actions/telegram/#prerequisites) in the Prerequisites section.
3. Set the <token> mentioned in the above link as the `TELEGRAM_BOT_ACCESS_TOKEN` secret for the repo.
4. Set the <to> mentioned in the above link as the `TELEGRAM_BOT_CHAT_ID` secret for the repo.
5. Set these secrets too: `JIIT_USERNAME`, `JIIT_PASSWORD`
6. Adjust the cron timing in the workflow file. (Optional)


### Gmail
Oauth tokens need to be saved in each workflow run for the subsequent runs. I haven't implemented that yet.


### Whatsapp
Whatsapp doesn't work right now through Github actions because the API access is shit.

<del>
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
</del>

## Note
This project uses a slightly modified version of [pyjiit](https://github.com/codelif/pyjiit)

The `pyjiit.wrapper.WebPortal.__hit()` method is modified to not raise an error on the failure response by the server. Failure response implies add drop option is not available.


## Future
Email and Telegram alerts.
