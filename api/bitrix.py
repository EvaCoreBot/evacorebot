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
        if hasattr(request, 'get_json'):
            event = request.get_json()
        elif isinstance(request, dict):
            body = request.get("body")
            if body is not None:
                event = json.loads(body)
            else:
                event = request
        else:
            raise ValueError("Unsupported request format")
    except Exception:
        return {"statusCode": 400, "body": "Invalid request"}

    params = event.get("data", {}).get("PARAMS", {})
    message = params.get("MESSAGE")
    dialog_id = params.get("DIALOG_ID")
    if not message or not dialog_id:
        return {"statusCode": 200, "body": "No message"}

    openai.api_key = OPENAI_API_KEY
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
        )
        answer = response.choices[0].message.content
    except Exception as e:
        return {"statusCode": 502, "body": f"OpenAI API error: {str(e)}"}

    requests.post(
        f"{BITRIX_WEBHOOK}/imbot.message.add.json",
        json={"DIALOG_ID": dialog_id, "MESSAGE": answer},
    try:
        resp = requests.post(
            f"{BITRIX_WEBHOOK}/imbot.message.add.json",
            json={"DIALOG_ID": dialog_id, "MESSAGE": answer},
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        return {"statusCode": 502, "body": f"Failed to send message to Bitrix24: {str(e)}"}

    return {"statusCode": 200, "body": "ok"}

