from flask import Flask, render_template, request, redirect, url_for
import os
import sys
import time
import difflib
import sys
import traceback
import datetime
import json
import traceback
import pandas as pd
from morepop import *
from tophashtags import *
from locatetweet import *
from originalvsretweeted import *
from typeoftweet import *
from favcounts import *


app = Flask(__name__)


@app.route('/location_of_the_tweet/', methods=['GET', 'POST'])
def location_of_the_tweet():
    locatetweet = location_of_tweet()
    return render_template('lot.html', locatetweet=locatetweet)


@app.route('/popular/', methods=['GET', 'POST'])
def popular():
    popularity_of_hillary_clinton = pop()[0]
    popularity_of_donald_trump = pop()[1]
    return render_template(
        'pop.html',
        popularity_of_hillary_clinton=popularity_of_hillary_clinton,
        popularity_of_donald_trump=popularity_of_donald_trump)


@app.route('/top_hashtags/', methods=['GET', 'POST'])
def top_hashtags():
    top_hashtags = top_ten_hashtags()
    return render_template('thash.html', top_hashtags=top_hashtags)


@app.route('/original_vs_retweeted/', methods=['GET', 'POST'])
def original_vs_retweeted():
    retweeted_count = original_vs_retweet()[0]
    original_count = original_vs_retweet()[1]
    return render_template(
        'ovr.html',
        retweeted_count=retweeted_count,
        original_count=original_count)


@app.route('/fav_counts/', methods=['GET', 'POST'])
def fav_counts():
    fav_count = favorite_counts()
    return render_template('fc.html', fav_count=fav_count)


@app.route('/type_of_tweet/', methods=['GET', 'POST'])
def type_of_tweet():
    text_count = types_of_tweet()[0]
    image_count = types_of_tweet()[1]
    text_and_image_count = types_of_tweet()[2]
    return render_template(
        'tot.html',
        text_count=text_count,
        image_count=image_count,
        text_and_image_count=text_and_image_count)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if request.form['action'] == 'Location of the Tweet':
            return redirect(url_for('location_of_the_tweet'))
        elif request.form['action'] == 'Popular':
            return redirect(url_for('popular'))
        elif request.form['action'] == 'Top Hashtags':
            return redirect(url_for('top_hashtags'))
        elif request.form['action'] == 'Original vs Retweeted':
            return redirect(url_for('original_vs_retweeted'))
        elif request.form['action'] == 'Favourite Counts':
            return redirect(url_for('fav_counts'))
        elif request.form['action'] == 'Type of Tweet':
            return redirect(url_for('type_of_tweet'))
    elif request.method == 'GET':
        return render_template('form_submit.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
