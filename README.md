# schedule
A schedule generator.

A background worker reads an excel source and generates an HTML page using jinja then caches it in redis.
The frontend (flask) serves via the redis cache.

Uses Heroku for hosting.

### required packages
```shell
pip3 install openpyxl
pip3 install flask
pip3 install gunicorn
```

### running the app (dev)
```shell
export FLASK_APP=schedule.py
```
```shell
python3 -m flask run
```

### running the app (prod)
```shell
python3 -m gunicorn.app.wsgiapp schedule:app
```