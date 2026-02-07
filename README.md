# Telegram Echo Bot

## Возможности

- Отвечает на все входящие сообщения, включая текст, стикеры и GIF.
- Команда `/start` показывает приветствие.

## Setup

1. Create a Telegram bot with @BotFather and copy the token.
2. Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Create a `.env` file with the bot token:

```bash
TELEGRAM_BOT_TOKEN="YOUR_TOKEN"
```

4. Run the bot:

```bash
python bot.py
```

The bot will echo back any message it receives.
