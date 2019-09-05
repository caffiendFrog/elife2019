import json
import os

import logging
import requests
import sys
import random

formatter = '[%(asctime)-15s] %(levelname)s [%(filename)s.%(funcName)s#L%(lineno)d] - %(message)s'

logging.basicConfig(level = logging.DEBUG, format = formatter)

# Create logger instance
logger = logging.getLogger('api')
resp_path = os.path.abspath("sample_data.json")

answers = []

def get_text(path):
	articles = {}
	try:
		with open(path, "r") as store:
			articles = json.load(store)
			store.close()
	except (IOError, OSError):
		return articles
	return articles


def get_random_article():
    articles = get_text(resp_path)
    if not articles:
        return None
    articles = list(articles.values())

    idx = random.randint(0, len(articles) -1)
    return articles[idx]