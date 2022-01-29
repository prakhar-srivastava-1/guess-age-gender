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
    print(guesses.get_predictions(name))
    age = 12
    gender = 'male'
    nationality = 'Indian'
    return render_template("guess.html",
                           name=name,
                           age=age,
                           gender=gender,
                           nationality=nationality)


if __name__ == "__main__":
    app.run(debug=True)