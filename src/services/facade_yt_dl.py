import os
from configuration import *


def download_yt(url: str, temp_name: str, ydl_opts: dict, extension: str):
    try:
        import youtube_dl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_infos = ydl.extract_info(url)

            video_name = '{}.{}'.format(video_infos['title'], extension)
            video_name = video_name.replace('//', '_').replace(':', '_').replace('|', '_').replace('"', "'")

            video_path = os.path.join(VIDEO_PATH, temp_name)

    except Exception as e:
        logger.error(e)

    finally:
        return video_path, video_name


def download_yt_video(url: str, temp_name: str):
    ydl_opts = {
        'outtmpl': '{}/{}'.format(VIDEO_PATH, temp_name),
        'logger': logger
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
        }],
        'logger': logger
    }
    return download_yt(url=url, ydl_opts=ydl_opts, temp_name=temp_name, extension='mp3')
