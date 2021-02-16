.. raw:: html

    <p align="center">
        <a href="#readme">
            <img alt="Loguru logo" src="https://github.com/org-de-familia/pytube-downloader/blob/main/docs/source/static/pytube-logo.png?raw=true">
        </a>
    </p>
    <p align="center">
    <a href="https://travis-ci.com/github/org-de-familia/pytube-downloader"><img alt="Travis CI" src="https://travis-ci.com/org-de-familia/pytube-downloader.svg?branch=main"></a>    
    <a href="https://telegram.me/pytube_downloader_bot"><img alt="chatroom icon" src="https://patrolavia.github.io/telegram-badge/chat.png"></a>
    <a href="https://dashboard.heroku.com/apps/pytube-downloader"><img alt="chatroom icon" src="https://heroku-badge.herokuapp.com/?app=pytube-downloader"></a>
    
    <p/>

==================

- **Link**: https://pytube-downloader.herokuapp.com/
- **Description**: Web environement and Telegram Bot for ``youtube_dl``
- **Objective**: Provides facility to download Youtube media 
- **Date**: 15/02/2021
- **Authors**: 
    - `@hrszanini <https://github.com/hrszanini>`_ | <hrszanini@gmail.com>
    - `@augustoliks <https://github.com/augustoliks>`_ | <carlos.neto.dev@gmail.com>
- **Actual Features**:
    - Download mp4 from Youtube Link;
    - Download mp3 from Youtube Link;
    - Telegram Bot;

Project Structure
-----------------

.. code-block:: bash

    ├── docker-compose.yaml
    ├── Dockerfile
    ├── docs
    │   └── source
    │       └── static
    │           └── pytube-logo.png
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.rst
    ├── requirements.txt
    └── src
        ├── configuration
        │   └── __init__.py
        ├── controllers
        │   ├── __init__.py
        │   └── routes.py
        ├── resources
        │   ├── css
        │   │   └── styles.css
        │   ├── html
        │   │   └── index.html
        │   ├── img
        │   │   └── pytube_logo.png
        │   └── js
        │       └── script.js
        ├── run.py
        └── services
            ├── facade_yt_dl.py
            ├── __init__.py
            ├── telegram_bot.py
            └── video_manager.py

Developers Guide
----------------

Add new dependency:

.. code-block:: bash

    poetry add DEPENDENCY
    poetry export -f requirements.txt > requirements.txt

Setup environement for development

.. code-block:: bash

    docker-compose up --build -d
