## Hi there 👋

<!--
**EvaCoreBot/evacorebot** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
### Bitrix24 GPT Bot

Файл `bitrix_bot.py` содержит обработчик webhook для облачной версии Bitrix24.
Он принимает входящие события, отправляет текст запроса в OpenAI и
отправляет ответ обратно в чат Bitrix24.

Переменные окружения:

- `BITRIX_WEBHOOK_URL` – адрес webhook, например
  `https://tdroks.bitrix24.ru/rest/1/2bcd7uxhgphx8v14`
- `OPENAI_API_KEY` – ключ доступа к OpenAI.

Запускайте функцию в совместимом сервере (Flask/Vercel/AWS Lambda),
чтобы принимать POST‑запросы от Bitrix24.

### Развёртывание на Render

1. Подготовьте репозиторий с исходным кодом и добавьте файл `.env.example`.
2. В панели управления Render нажмите **New Web Service** и выберите этот репозиторий.
3. Укажите настройки:
   - **Environment** – `Python`.
   - **Build Command** – `pip install -r requirements.txt`.
   - **Start Command** – `python3 eva_bot.py`.
4. В разделе **Environment Variables** добавьте значения `TELEGRAM_TOKEN`,
   `OPENAI_API_KEY`, `BITRIX_WEBHOOK_URL` и другие переменные из `.env.example`.
5. После нажатия **Create Web Service** Render соберёт контейнер и запустит
   бота в постоянном режиме.

Для запуска REST‑обработчика Bitrix24 создайте отдельный сервис с командой
`python3 api/bitrix_bot.py` и теми же переменными окружения.
