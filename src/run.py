import logging
from configuration import *

import fastapi
import uvicorn
import os

import controllers
import services

logger.setLevel(logging.DEBUG)

app = fastapi.FastAPI()
video_manager = services.FilesManager()
controllers.configure_routes(app=app, video_manager=video_manager)

if os.environ.get('TEST_ENV'):
    uvicorn.run(app, host="0.0.0.0", port=5000)
