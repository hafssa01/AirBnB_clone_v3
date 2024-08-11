#!/usr/bin/python3
"""
Creation of Flask app blueprint
"""
from flask import Blueprint

app_views = Blueprint

from api.v1.views.index import *