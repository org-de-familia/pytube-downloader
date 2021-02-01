import os
import youtube_dl
import configuration
from loguru import logger


VIDEO_PATH = os.path.join(os.getcwd(), configuration.VIDEO_PATH)


def download_yt(url: str, temp_name: str, ydl_opts: dict, extension: str):
    new_name = None
    video_name = None

    try:
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_infos = ydl.extract_info(url)

            video_name = '{}.{}'.format(video_infos['title'], extension)  # video_infos['id']
            video_name = video_name.replace('//', '_').replace(':', '_').replace('|', '_').replace('"', "'")

            old_name = os.path.join(VIDEO_PATH, temp_name)
            new_name = os.path.join(VIDEO_PATH, video_name)

            os.rename(old_name, new_name)

    except Exception as e:
        logger.error(e)

    finally:
        return new_name, video_name


def download_yt_video(url: str, temp_name: str):
    ydl_opts = {
        'outtmpl': '{}/{}'.format(VIDEO_PATH, temp_name)
    }
    return download_yt(url=url, ydl_opts=ydl_opts, temp_name=temp_name, extension='mp4')


def download_yt_audio(url: str, temp_name: str):
    ydl_opts = {
        'outtmpl': '{}/{}'.format(VIDEO_PATH, temp_name),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    return download_yt(url=url, ydl_opts=ydl_opts, temp_name=temp_name, extension='mp3')
