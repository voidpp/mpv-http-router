import json
import logging

logger = logging.getLogger(__name__)

class Message():

    def __init__(self, id: str, data, error: str = ''):
        self._id = id
        self._data = data
        self._error = error

    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self._error

    @staticmethod
    def create(raw_message: str) -> 'Message':
        try:
            raw_data = json.loads(raw_message)
        except ValueError as e:
            logger.error("malformed message: %s", e)
            return None

        try:
            id = raw_data['id']
            data = raw_data['data']
        except KeyError as e:
            logger.error("malformed message: %s", e)
            return None

        return Message(id, data)

    def __str__(self):
        return json.dumps({'id': self._id, 'data': self._data})
