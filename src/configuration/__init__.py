import logging
import os

VIDEO_PATH = os.path.join(os.getcwd(), 'videos')
RESOURCES_PATH = 'resources'
LOG_FILE = './logfile.log'
BOT_TOKEN = os.environ.get('BOT_TOKEN')

logging.basicConfig(filename=LOG_FILE,
                    filemode="w+",
                    format="%(message)s")

logger = logging.getLogger("my_logger")


__all__ = ["logger", "VIDEO_PATH", "RESOURCES_PATH", "LOG_FILE"]
