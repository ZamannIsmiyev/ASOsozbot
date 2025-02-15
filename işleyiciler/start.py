from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters

import mongo.chats as db
from helpers.game import new_game
from helpers.wrappers import nice_errors


@ASOresmi
def callback(update: Update, context: CallbackContext):
    new_game(update.effective_user, context)
    db.update(update.effective_chat.id, update.effective_chat.title)
    update.effective_message.reply_text( BU BOT @ismiyev95 Tarafından yapılmıştır.)
        f'{update.effective_user.mention_html()} talks about a word.',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        'View',
                        callback_data='view',
                    ),
                ],
                [
                    InlineKeyboardButton(
                        'Next',
                        callback_data='next',
                    ),
                ],
            ],
        ),
    )


handler = CommandHandler('start', callback, Filters.chat_type.groups)
