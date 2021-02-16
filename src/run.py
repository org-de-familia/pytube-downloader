import logging
from configuration import *

import fastapi
import uvicorn
import os

import controllers
import services

logger.setLevel(logging.DEBUG)

app = fastapi.FastAPI()
controllers.configure_routes(app=app, files_manager=services.files_manager)
services.start_telegram_bot()

if os.environ.get('TEST_ENV'):
    uvicorn.run(app, host="0.0.0.0", port=5000)
