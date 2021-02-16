from uuid import uuid4

import configuration
from configuration import logger
import services
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler


HELP_MESSAGE = "Comandos disponíveis:\n" \
               "/audio {link do YouTube}: extrai o áudio do link e retorna como arquivo MP3 (.mp3)\n" \
               "/video {link do YouTube}: baixa vídeo e retorna como arquivo MP4 (.mp4)\n" \
               "/help: informa os comandos e suas funcionalidades.\n" \
               "Caso o bot seja citado com @pytube_downloader_bot {link do YouTube}, " \
               "serão apresentadas 2 opções para autopreenchimento dos comandos."


def process_request(msg, command):
    msg = msg.replace('@pytube_downloader_bot', '')
    msg = msg.replace(f'/{command} ', '')
    return msg


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Seja bem vindo ao PyTubeDownloader.\n{HELP_MESSAGE}')


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{HELP_MESSAGE}')


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


def inlinequery(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    results = []

    if query.startswith('http://') or query.startswith('https://'):
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=f'Video',
                input_message_content=InputTextMessageContent(
                    f"/video {query} ", parse_mode=ParseMode.MARKDOWN
                ),
            ),
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=f'Audio',
                input_message_content=InputTextMessageContent(
                    f"/audio {query} ", parse_mode=ParseMode.MARKDOWN
                ),
            )
        ]

    update.inline_query.answer(results=results)


def start_telegram_bot():
    updater = Updater(configuration.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("audio", download_audio))
    dispatcher.add_handler(CommandHandler("video", download_video))

    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()
