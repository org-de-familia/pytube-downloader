import fastapi

import services
import configuration


def configure_routes(app: fastapi.FastAPI, video_manager: services.VideoManager):

    @app.get('/video/download')
    def get_download_video(url: str):
        file_path, file_name = video_manager.get_video(url)
        return fastapi.responses.FileResponse(file_path, media_type='video/mp4', filename=file_name)

    @app.get('/audio/download')
    def get_download_audio(url: str):
        file_path, file_name = video_manager.get_audio(url)
        return fastapi.responses.FileResponse(file_path, media_type='audio/mp3', filename=file_name)

    @app.get('/')
    def home_page():
        html_file_path = '{}/html/index.html'.format(configuration.RESOURCES_PATH)
        return fastapi.responses.HTMLResponse(open(html_file_path, 'r', encoding='utf8').read())

    @app.get('/css/{file}')
    def css_file(file: str):
        css_file_path = '{}/css/{}'.format(configuration.RESOURCES_PATH, file)
        return fastapi.responses.HTMLResponse(open(css_file_path, 'r', encoding='utf8').read())

    @app.get('/js/{file}')
    def css_file(file: str):
        js_file_path = '{}/js/{}'.format(configuration.RESOURCES_PATH, file)
        return fastapi.responses.HTMLResponse(open(js_file_path, 'r', encoding='utf8').read())
