import json
import requests
from django.conf import settings


def checkout(payload):
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.paystack.co/transaction/initialize",
        headers=headers,
        data=json.dumps(payload)
    )

    response_data = response.json()

    if response_data.get("status") is True:
        return True, response_data["data"]["authorization_url"]
    else:
        return False, response_data.get("message", "Failed to initiate payment.")
