import os
from telegram.ext import ApplicationBuilder, CommandHandler

from doc_handler import handle_doc
from risk_handler import handle_risk
from review_handler import handle_review
from prompt_handler import handle_prompt


async def start(update, context):
    await update.message.reply_text(
        "Eva.Юрист подключена. Команды: /doc /risk /review /prompt"
    )


def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN is not set")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("doc", handle_doc))
    app.add_handler(CommandHandler("risk", handle_risk))
    app.add_handler(CommandHandler("review", handle_review))
    app.add_handler(CommandHandler("prompt", handle_prompt))
    app.run_polling()


if __name__ == "__main__":
    main()