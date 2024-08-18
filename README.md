# Realtime Chat Application

This is a realtime chat application built with Django, Django Channels, and Redis. The application allows users to create chat rooms and exchange messages in real-time.

## Features

- Real-time messaging using WebSockets
- User authentication (login and logout)
- Creation and management of chat rooms
- Message persistence in SQLite database
- Scalable WebSocket handling using Redis

## Requirements

- Python 3.8+
- Django 5.1
- Redis 7.4.0

## Dependencies

- `asgiref` 3.8.1
- `channels` 4.1.0
- `channels-redis` 4.2.0
- `daphne` 4.1.2
- `sqlparse` 0.5.1
- `tzdata` 2024.1
### Additional Dependencies

For completeness, the project also includes:
- `attrs`, `autobahn`, `Automat`, `cffi`, `constantly`, `cryptography`, `hyperlink`, `idna`, `incremental`, `msgpack`, `pyasn1`, `pyasn1_modules`, `pycparser`, `pyOpenSSL`, `redis`, `service-identity`, `Twisted`, `txaio`, `typing_extensions`, `zope.interface`

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt

### Clone the Repository

 ```bash
    git clone https://github.com/KamilCecko/Realtime-Chat-Application