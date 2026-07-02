import base64
import json
import time
from datetime import datetime


def decode_token(token: str) -> dict:
    parts = token.split('.')
    # print(parts)
    # Add missing padding mathematically
    payload_string = parts[1] + "=" * (-len(parts[1]) % 4)
    payload = base64.b64decode(payload_string)
    data = json.loads(payload)
    # print('TOKEN DATA', data)
    return data


def token_expired(token: str):
    data = decode_token(token)
    expiration = data.get('exp')
    # user = data.get('user')
    # token_expire_date = datetime.fromtimestamp(expiration)
    ctime = int(time.time())
    return ctime > expiration

