import fastapi
import uvicorn

import controllers
import services
import os


app = fastapi.FastAPI()
video_manager = services.FilesManager()
controllers.configure_routes(app=app, video_manager=video_manager)


if os.environ.get('TEST_ENV'):
    uvicorn.run(app, host="0.0.0.0", port=5000)
