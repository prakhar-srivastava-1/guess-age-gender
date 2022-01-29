import datetime
from flask import Flask, render_template
from api import GuessifyApi

app = Flask(__name__)


@app.route("/")
def index():
    year = datetime.datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guessify(name):
    guesses = GuessifyApi()
    predictions = guesses.get_predictions(name)
    age = predictions[1]['age']
    gender = predictions[0]['gender']
    nationality = predictions[2]['country'][0]['country_id']
    return render_template("guess.html",
                           name=name,
                           age=age,
                           gender=gender,
                           nationality=nationality)


if __name__ == "__main__":
    app.run(debug=True)