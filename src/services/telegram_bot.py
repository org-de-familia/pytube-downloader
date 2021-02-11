from uuid import uuid4

import configuration
from configuration import logger
import services
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, ParseMode, InlineQueryResultVoice
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler
from py_de_familia import clidefamilia


def process_request(msg, command):
    msg = msg.replace('@pytube_downloader_bot', '')
    msg = msg.replace(f'/{command} ', '')
    return msg


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def download_audio(update: Update, context: CallbackContext) -> None:
    params = process_request(update.message.text, 'audio')
    logger.debug(f'AUDIO: {params}')
    file_path, file_name = services.files_manager.get_audio(params)
    update.message.reply_audio(audio=open(file_path, 'rb'), filename=file_name)


def download_video(update: Update, context: CallbackContext) -> None:
    params = process_request(update.message.text, 'video')
    logger.debug(f'VIDEO: {params}')
    file_path, file_name = services.files_manager.get_video(params)
    update.message.reply_video(video=open(file_path, 'rb'), filename=file_name)


def pdf(update: Update, context: CallbackContext) -> None:
    params = process_request(update.message.text, 'pdf').split(' ')
    logger.debug(f'PDF: {params}')
    audio_path = clidefamilia.obter_audio_de_familia(params[0], params[1])
    update.message.reply_voice(voice=open(audio_path, 'rb'))


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    chars_de_familia = clidefamilia.listar_personagens_de_familia()

    results = []

    for char in chars_de_familia:
        for frase in clidefamilia.obter_frases_de_familia(char):
            results.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=f'{char} {frase}',
                    input_message_content=InputTextMessageContent(
                        f"/pdf {char} {frase} ", parse_mode=ParseMode.MARKDOWN
                    ),
                )
            )

    update.inline_query.answer(results=results)


def start_telegram_bot():
    updater = Updater(configuration.BOT_TOKEN)
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("audio", download_audio))
    dispatcher.add_handler(CommandHandler("video", download_video))
    dispatcher.add_handler(CommandHandler("pdf", pdf))

    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()
