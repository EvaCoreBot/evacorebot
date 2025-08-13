import os
import json
import openai
import requests

BITRIX_WEBHOOK = os.getenv("BITRIX_WEBHOOK")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def handler(request):
    """Handle Bitrix24 webhook events and respond using OpenAI."""
    if not BITRIX_WEBHOOK or not OPENAI_API_KEY:
        return {"statusCode": 500, "body": "Missing configuration"}

    try:
        # Try to parse the request payload
        event = request.get_json() if hasattr(request, 'get_json') else json.loads(request["body"])
    except Exception:
        return {"statusCode": 400, "body": "Invalid request"}

    params = event.get("data", {}).get("PARAMS", {})
    message = params.get("MESSAGE")
    dialog_id = params.get("DIALOG_ID")
    if not message or not dialog_id:
        return {"statusCode": 200, "body": "No message"}

    # Send message to OpenAI ChatCompletion
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    answer = response.choices[0].message.content

    # Respond back to Bitrix
    requests.post(
        f"{BITRIX_WEBHOOK}/imbot.message.add.json",
        json={"DIALOG_ID": dialog_id, "MESSAGE": answer},
    )

    return {"statusCode": 200, "body": "ok"}
