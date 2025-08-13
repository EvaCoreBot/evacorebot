from telegram import Update
from telegram.ext import ContextTypes

async def handle_risk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📊 Таблица рисков:\n"
        "| № | Риск | Последствия | Вероятность | Влияние | Меры |\n"
        "|---|------|-------------|-------------|---------|------|\n"
        "| 1 | Срыв сроков | Потеря клиента | Средняя | Высокое | Штрафы в договоре |"
    )
    await update.message.reply_text(text)