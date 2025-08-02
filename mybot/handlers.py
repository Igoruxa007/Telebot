from random import randint, choice
from telegram import Update
from emoji import emojize
from telegram.ext import ContextTypes

from utils import main_keyboard, main_keyboard1


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


async def add_user_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    location = update.message.location
    context.user_data['last_location'] = location
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Your location is {location}'
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