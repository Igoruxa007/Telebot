from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters, CommandHandler
from telegram import Update, ReplyKeyboardMarkup


async def start_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [['1', '2', '3']]

    await update.message.reply_text(
        "Chose number",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Number&"
        ),
    )

    return 'number'


async def number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [['red', 'green', 'blue']]
    user = update.message.from_user
    print(f'{user} number = {update.message.text}')
    await update.message.reply_text(
        "Chose color",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="ColoR"
        )
    )

    return 'color'


async def color(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [['100', '200', '300']]
    user = update.message.from_user
    print(f'{user} color = {update.message.text}')
    await update.message.reply_text(
        "Chose speed",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="SpeeD"
        )
    )

    return 'speed'


async def speed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    print(f'{user} speed = {update.message.text}')
    await update.message.reply_text(
        "End of conversation",
    )

    return ConversationHandler.END


async def anketa_dontknow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        'Unknown command'
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Bye",
    )

    return ConversationHandler.END

anketa = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex('^(1)$'), start_conversation)
    ],
    states={
        'number': [MessageHandler(filters.TEXT, number)],
        'color': [MessageHandler(filters.TEXT, color)],
        'speed': [MessageHandler(filters.TEXT, speed)],
    },
    fallbacks=[
        MessageHandler(filters.TEXT | filters.PHOTO | filters.VIDEO | filters.LOCATION, anketa_dontknow),
        CommandHandler('cancel', cancel)
    ]
)