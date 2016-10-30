from flask import Flask, render_template, request, redirect, url_for
import os
import sys
import time
import difflib
import sys, traceback
import datetime
import traceback

app = Flask(__name__)


@app.route('/location_of_the_tweet/', methods=['GET', 'POST'])
def location_of_the_tweet():
	return render_template('lot.html')


@app.route('/popular/', methods=['GET', 'POST'])
def popular():
	os.system('python morepop.py')
	return render_template('pop.html')


@app.route('/top_hashtags/', methods=['GET', 'POST'])
def top_hashtags():
	return render_template('thash.html')


@app.route('/original_vs_retweeted/', methods=['GET', 'POST'])
def original_vs_retweeted():
	return render_template('ovr.html')


@app.route('/fav_counts/', methods=['GET', 'POST'])
def fav_counts():
	return render_template('fc.html')


@app.route('/type_of_tweet/', methods=['GET', 'POST'])
def type_of_tweet():
	return render_template('tot.html')


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


if __name__ == "__main__" :
	app.debug=True
	app.run()
