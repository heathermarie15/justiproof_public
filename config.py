import os
from dotenv import load_dotenv


class Config(object):
    SECRET_KEY = os.getenv('APP_SECRET_KEY')