# Telegram Echo Bot

## Возможности

- Отвечает текстом на все входящие сообщения (включая подписи к медиа).
- Команда `/start` показывает приветствие.

## Setup

1. Create a Telegram bot with @BotFather and copy the token.
2. Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Export the token and run the bot:

```bash
export TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
python bot.py
```

The bot will echo back any text message it receives.
