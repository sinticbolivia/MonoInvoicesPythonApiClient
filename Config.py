import os
import json
from odoo.addons.siat_client import constants
from abc import ABC
import copy


class Config(ABC):

    def __init__(self):
        self._filename = '{0}/config.json'.format(constants.DATA_DIR)
        self.server = None
        self.username = None
        self.password = None
        self.token = None

    def to_dict(self):

        data = copy.deepcopy(self.__dict__)

        if '_filename' in data:
            data.pop('_filename')

        return data

    def to_json(self):
        json_str = json.dumps(self.to_dict())

        return json_str

    def load(self):
        print('LOADING CONFIG FILE: ', self._filename)
        data = None
        if os.path.isfile(self._filename):
            try:
                with open(self._filename, 'r') as file:
                    data = json.load(file)
            except Exception as e:
                print('LOADING CONFIG ERROR: ', str(e))

        print("JSON DATA", data)

        if data is None:
            return

        self.server = data.get('server', '')
        self.username = data.get('username', '')
        self.password = data.get('password', '')
        self.token = data.get('token', '')

    def save(self):
        print('SAVING CONFIG: ', self.to_json())
        with open(self._filename, 'w') as file:
            file.write(self.to_json())

    @staticmethod
    def get_instance():
        obj = Config()
        obj.load()

        return obj
