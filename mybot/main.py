import logging
import os
from dotenv import load_dotenv
from random import randint, choice
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize
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


def main_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return ReplyKeyboardMarkup([['Прислать смайлик'], [KeyboardButton('My coord', request_location=True)]])


def main_keyboard1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return ReplyKeyboardMarkup([['Прислать смайлик', 'Прислать смайлик'], ['Прислать смайлик']])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user.first_name
    if 'status' in context.user_data:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            reply_markup=main_keyboard(update, context),
            text=f"Hello {user}! Your status is {context.user_data['status']}",
        )
    else:
        context.user_data['status'] = 'Admin'
        USER_EMOJI = [':cat:', ':smile:', ':panda:', ':dog:']
        smile = choice(USER_EMOJI)
        smile = emojize(smile)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello {user}! I am your bot. Send me a message, and I will echo it back. {smile}",
        )


async def send_smile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    USER_EMOJI = [':cat:', ':smile:', ':panda:', ':dog:']
    smile = emojize(choice(USER_EMOJI))
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{smile}",
        reply_markup=main_keyboard1(update, context),
    )


async def square(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        try:
            user_number = int(context.args[0])
            message = user_number**2
        except (TypeError, ValueError):
            message = "Wrong value"
    else:
        message = "Введите число"
    await update.message.reply_text(message)


async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_number = int(context.args[0])
    except (TypeError, ValueError):
        message = "Wrong input"
    bot_number = randint(user_number - 10, user_number + 10)
    message = f"My number is {bot_number}, your number is {user_number}, "
    if bot_number > user_number:
        message += "i won"
    elif bot_number < user_number:
        message += " you won"
    elif bot_number == user_number:
        message += "draw"
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

    application.add_handler(CommandHandler("k", main_keyboard))

    application.add_handler(CommandHandler("s", send_smile))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_smile))

    logging.info("Bot started")

    application.run_polling()


if __name__ == "__main__":
    main()
