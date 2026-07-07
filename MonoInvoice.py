import requests

from . import Utils


class MonoInvoiceClient:

    def __init__(self):
        self._server = None
        self._base_url = None
        self._token = None
        self._config = None

    def set_config(self, cfg):
        self._config = cfg
        self.set_server()
        self.set_token(self._config.token)

    def get_config(self):
        return self._config

    def set_server(self, url: str = None):
        if url is not None:
            self._server = url
        else:
            self._server = self._config.server

        self._base_url = '{0}/api'.format(self._server)

    def _get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self._token)
        }

        return headers

    def get_token(self):
        return self._token

    def set_token(self, token):
        self._token = token

    def is_token_expired(self):
        return Utils.token_expired(self._token)


    def login(self):
        if self._config is None:
            raise Exception('Invalid Siat Client Config')
        if not self._config.username:
            raise Exception('Invalid Siat Client Username')
        if not self._config.password:
            raise Exception('Invalid Siat Client Password')

        endpoint = '{0}/users/get-token'.format(self._base_url)
        headers = {'Content-Type': 'application/json'}
        body = {'username': self._config.username, 'password': self._config.password}
        res = requests.post(endpoint, json=body, headers=headers)
        data = res.json()
        if data is None:
            raise Exception('Invalid login response.' + 'RESPONSE: ' + res.content)

        # print('STATUS CODE', res.status_code)
        if res.status_code != 200:
            raise Exception(data.get('error'))
        print(data)
        if data.get('data', {}) is None or 'token' not in data.get('data', {}):
            raise Exception('SIAT CLIENT LOGIN ERROR: Token not found in response')

        self._token = data.get('data', {}).get('token', None)
        self._config.token = self._token
        # print(self._token)
        return data
