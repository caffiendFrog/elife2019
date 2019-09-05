from flask import Flask, request, current_app, render_template
from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SelectMultipleField, SubmitField
import json
import requests
import os
import random

from . import api
from .utilities import get_random_article, make_choices

@api.route('/abstract/', methods = ['GET'])
def display_article():
    id, article = get_random_article()
    text = article.get('text', None)
    candidates = article.get('candidates', None)

    form = CandidateValidationForm()
    form.id = id
    form.candidates.choices = make_choices(candidates)
    form.text = text
    return render_template('index.html', id = id, candidates = candidates, message = text, form=form)
    

@api.route('/validate', methods = ['POST'])
def validate_equipment():
    pass


class CandidateValidationForm(FlaskForm):
    id = StringField('Article ID', render_kw={'readonly': True})
    text = TextAreaField('Article excerpt')
    candidates = SelectMultipleField('Candidates')
    submit = SubmitField('Confirm')