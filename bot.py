import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text(
        "Привет! Я эхо-бот. Отправь сообщение, и я отвечу тем же текстом."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None or update.effective_chat is None:
        return

    logger.info("Echoing message from user %s", update.effective_user.id)
    await update.message.copy(chat_id=update.effective_chat.id)


def main() -> None:
    load_dotenv()
    if update.message is None:
        return

    text = update.message.text or update.message.caption
    if not text:
        await update.message.reply_text("Я пока умею отвечать только на текстовые сообщения.")
        return

    logger.info("Echoing message from user %s", update.effective_user.id)
    await update.message.reply_text(text)


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, echo))

    application.run_polling()


if __name__ == "__main__":
    main()
