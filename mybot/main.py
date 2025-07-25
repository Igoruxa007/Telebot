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

logging.basicConfig(
    filename='bot.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! I am your bot. Send me a message, and I will echo it back.",
    )


async def square(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        try:
            user_number = int(context.args[0])
            message = user_number - 1
        except (TypeError, ValueError):
            message = "Wrong value"
    else:
        message = "Введите число"
    await update.message.reply_text(message)


async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        message = context.args[0]
    except (TypeError, ValueError):
        message = "Wrong text"
    await update.message.reply_text(message)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


def main() -> None:
    load_dotenv()

    application = (
        ApplicationBuilder()
        .token(token=os.getenv('TOKEN'))
        .build()
    )

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("square", square))

    application.add_handler(CommandHandler("guess", guess))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logging.info("Bot started")

    application.run_polling()


if __name__ == "__main__":
    main()
