from telegram.ext import ApplicationBuilder, CommandHandler
from modules.doc_handler import handle_doc
from modules.risk_handler import handle_risk
from modules.review_handler import handle_review
from modules.prompt_handler import handle_prompt

async def start(update, context):
    await update.message.reply_text("Eva.Юрист подключена. Команды: /doc /risk /review /prompt")

def handler(request):
    from telegram.ext import Application
    app = ApplicationBuilder().token("TOKEN_PLACEHOLDER").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("doc", handle_doc))
    app.add_handler(CommandHandler("risk", handle_risk))
    app.add_handler(CommandHandler("review", handle_review))
    app.add_handler(CommandHandler("prompt", handle_prompt))
    return {"statusCode": 200, "body": "Telegram webhook active"}