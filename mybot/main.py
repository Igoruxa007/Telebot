import logging
import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from handlers import (start, add_user_location, send_smile, square, guess, echo)


logging.basicConfig(
    filename='bot.log',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


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

    application.add_handler(CommandHandler("s", send_smile))

    application.add_handler(MessageHandler(filters.LOCATION, add_user_location))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logging.info("Bot started")

    application.run_polling()


if __name__ == "__main__":
    main()
