from datetime import datetime
from flask import Flask, render_template, request
from logging import DEBUG
from forms import ScrabbleForm, SpellBeeForm
from word_cheater import ScrabbleMain, SpellBeeMain

# call the Flask constructor
#application object

app = Flask(__name__)
app.secret_key = b'\x8d\x07t\xe3\xf4Q\xb1Y'
app.logger.setLevel(DEBUG)

feedbacks = []

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/scrabble2', methods=['GET', 'POST'])
def scrabble():
	form = ScrabbleForm()
	sorted_results = {}
	if request.method == "POST":
		rack = request.form['letters']
		word_filter = request.form['filter']
		sorted_results = ScrabbleMain(rack, word_filter)
	return render_template("scrabble2.html", form=form, columns=['Words'], sorted_results=sorted_results)


@app.route("/nyspellbee", methods=['GET', 'POST'])
def spellbee():
	form = SpellBeeForm()
	sorted_results_list = []
	if request.method == "POST":
		required_letter = request.form['required']
		other_letters = request.form['other']
		sorted_results_list = SpellBeeMain(required_letter, other_letters)
	return render_template("nyspellbee.html", form=form, columns=['Words'], sorted_results=sorted_results_list)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
