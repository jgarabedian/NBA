from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask(__name__)

from app import routes
# import os
# import logging
# logging

