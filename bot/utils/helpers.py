# Source
# https://github.com/python-telegram-bot/rules-bot/blob/master/util.py
import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.ext import CallbackContext

logger = logging.getLogger(__name__)
try:
    from bs4 import BeautifulSoup
except ImportError:
    logger.warning("BeautifulSoup not found, please dont use get_text_not_in_entities")


def get_reply_id(update):
    if update.message and update.message.reply_to_message:
        return update.message.reply_to_message.message_id
    return None


def reply_or_edit(update, context, text):
    chat_data = context.chat_data
    if update.edited_message:
        chat_data[update.edited_message.message_id].edit_text(
            text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
    else:
        issued_reply = get_reply_id(update)
        if issued_reply:
            chat_data[update.message.message_id] = context.bot.sendMessage(
                update.message.chat_id,
                text,
                reply_to_message_id=issued_reply,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
            )
        else:
            chat_data[update.message.message_id] = update.message.reply_text(
                text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
            )


def get_text_not_in_entities(html):
    soup = BeautifulSoup(html, "html.parser")
    return " ".join(soup.find_all(text=True, recursive=False))


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i : i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def truncate_str(str, max):
    return (str[:max] + "…") if len(str) > max else str


# https://github.com/python-telegram-bot/rules-bot/blob/master/components/inlinequeries.py
def article(title="", description="", message_text="", key=None, reply_markup=None):
    return InlineQueryResultArticle(
        id=key or uuid4(),
        title=title,
        description=description,
        input_message_content=InputTextMessageContent(
            message_text=message_text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        ),
        reply_markup=reply_markup,
    )
