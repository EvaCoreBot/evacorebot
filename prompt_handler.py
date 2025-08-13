from telegram import Update
from telegram.ext import ContextTypes

async def handle_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args).strip().lower()
    if query:
        await update.message.reply_text(f"🔍 Промт по теме «{query}»:\n(пример текста промта)")
    else:
        await update.message.reply_text("⚠️ Уточните тему: /prompt договор")