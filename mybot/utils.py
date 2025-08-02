from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


def main_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return ReplyKeyboardMarkup([['Прислать смайлик'], [KeyboardButton('My location', request_location=True)]])


def main_keyboard1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return ReplyKeyboardMarkup([['Прислать смайлик', 'Прислать смайлик'], ['Прислать смайлик']])