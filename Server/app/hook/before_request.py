from base64 import b64encode
from datetime import timedelta, datetime
from hashlib import sha3_512

from dateutil.parser import parse
from flask import request, abort, current_app


def kst_now():
    return datetime.utcnow() + timedelta(hours=9)


def check_secret_header():
    if current_app.config['TESTING']:
        return
    if request.method == 'OPTIONS':
        return
    if request.endpoint in ['flasgger.static', 'flasgger.apidocs', 'flassger.apispec', 'flasgger.apispec_1']:
        return

    date = request.headers.get('X-Date')
    user_agent = request.headers.get('User-Agent')
    secret = request.headers.get('User-Data')

    if None in (date, user_agent, secret):
        abort(418)

    key = (user_agent + date).encode()
    h = sha3_512(b64encode(key)).hexdigest()
    request_date = parse(date)

    if not (kst_now() - timedelta(minutes=1) <= request_date <= kst_now() + timedelta(minutes=1) and h == secret):
        abort(418)
