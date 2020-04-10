import urllib.request
import io
import openpyxl
import datetime
import os
import redis

from flask import Flask, request
from talisman import Talisman

app = Flask(__name__)
Talisman(app)

try:
    rdb = redis.from_url(os.environ.get('REDIS_URL'))
except:
    rdb = redis.Redis()

DisableCache = [('Cache-Control', 'no-cache, no-store, must-revalidate'), ('Pragma', 'no-cache'), ('Expires', '0')]

CONFIG_USER = '...'
CONFIG_PASS = '...'

def route(date):
    auth = request.authorization
    if not auth or auth['username'] != CONFIG_USER or auth['password'] != CONFIG_PASS:
        return 'Not Authorized', 401, [('WWW-Authenticate', 'Basic')]
    view = rdb.get(str(date))
    if view: return view, 200, DisableCache
    return 'Cache is not yet built for this date, either it is warming up, or not yet supported.', 200, DisableCache

@app.route('/<int:year>-<int:month>-<int:day>')
def route_with_date(year, month, day):
    return route(datetime.date(year, month, day))

@app.route('/')
def default_route():
    return route(datetime.date.today())
