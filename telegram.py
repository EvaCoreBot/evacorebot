import os
from telegram.ext import ApplicationBuilder, CommandHandler

from doc_handler import handle_doc
from risk_handler import handle_risk
from review_handler import handle_review
from modules.doc_handler import handle_doc
from modules.risk_handler import handle_risk
from modules.prompt_handler import handle_prompt

async def start(update, context):
    await update.message.reply_text("Eva.Юрист подключена. Команды: /doc /risk /review /prompt")

def handler(request):
    from telegram.ext import Application
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN environment variable is not set.")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("doc", handle_doc))
    app.add_handler(CommandHandler("risk", handle_risk))
    app.add_handler(CommandHandler("review", handle_review))
    app.add_handler(CommandHandler("prompt", handle_prompt))
    return {"statusCode": 200, "body": "Telegram webhook active"}
