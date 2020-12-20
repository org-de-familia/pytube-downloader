import os
import threading
import time
from datetime import datetime

from loguru import logger

import configuration
import services


class Video:
    name: str
    file_path: str
    time: int


class VideoManager:
    videos = {}

    def __init__(self):
        self.temp_name = self.temporary_name()
        self.clean_video_path()
        threading.Thread(target=self.run).start()

    def get_video(self, url):
        url = url.replace('"', '')

        if url not in self.videos.keys() or self.videos[url].name is None:
            temp_file_name = next(self.temp_name)

            video = Video()
            video.file_path, video.name = services.yt_services.download_yt_video(url=url, temp_name=temp_file_name)
        else:
            video = self.videos[url]

        video.time = datetime.now().timestamp()
        self.videos[url] = video

        return video.file_path, video.name

    def run(self):
        sleep_time = 5 * 60
        while True:
            now = datetime.now().timestamp()
            videos_to_remove = []

            for url in self.videos.keys():
                video = self.videos[url]
                if now - video.time >= sleep_time:
                    try:
                        logger.info('Removing: {video_name}'.format(video_name=video.name))
                        video.name = None
                        os.remove(video.file_path)
                        videos_to_remove.append(url)
                    except Exception as e:
                        logger.error(e)

            for url in videos_to_remove:
                self.videos.pop(url)

            time.sleep(sleep_time)

    @staticmethod
    def temporary_name():
        count = 0
        while True:
            yield str(count)
            count += 1

    @staticmethod
    def clean_video_path():
        try:
            video_path = os.path.join(os.getcwd(), configuration.VIDEO_PATH)
            for file in os.listdir(video_path):
                file_path = os.path.join(video_path, file)
                os.remove(file_path)
                logger.info('Removing {}'.format(file_path))
        except Exception as e:
            logger.info(e)
