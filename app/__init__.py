__package__ = 'app'

from flask import Flask

app = Flask(__name__)

from router import router

