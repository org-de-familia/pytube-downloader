import os
import youtube_dl
import configuration
from loguru import logger


def download_yt_video(url: str, temp_name: str):
    new_name = None
    video_name = None

    try:
        video_path = os.path.join(os.getcwd(), configuration.VIDEO_PATH)
        ydl_opts = {'outtmpl': '{}/{}'.format(video_path, temp_name)}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_infos = ydl.extract_info(url)

            video_name = '{}.mp4'.format(video_infos['title'], video_infos['id'])
            video_name = video_name.replace('//', '_').replace(':', '_').replace('|', '_').replace('"', "'")

            old_name = os.path.join(video_path, temp_name)
            new_name = os.path.join(video_path, video_name)

            os.rename(old_name, new_name)

    except Exception as e:
        logger.error(e)

    finally:
        return new_name, video_name
