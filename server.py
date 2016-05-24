import os

from flask import Flask
from redis import StrictRedis


app = Flask(__name__)
redis_server = os.environ.get('REDIS_SERVER')
redis = StrictRedis(host=redis_server, port=6379, db=0)
KEY = "master_key"


@app.route("/")
def increment():
    redis.incr(KEY)
    return redis.get(KEY)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
