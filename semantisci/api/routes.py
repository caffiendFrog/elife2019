from flask import Flask, request, current_app, render_template
import json
import requests
import os
import random

from . import api
from .utilities import get_random_article

@api.route('/abstract/', methods = ['GET'])
def display_article():
    article = get_random_article()
    text = article.get('text', None)
    candidates = article.get('candidates', None)
    print (text, candidates)
    

@api.route('/validate', methods = ['POST'])
def validate_equipment():
    pass    