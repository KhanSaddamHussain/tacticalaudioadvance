from flask import Flask, render_template
import json
with open('config.json', 'r') as c:
    params = json.load(c)["parameters"]

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="home")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", title="portfolio")

@app.route('/services')
def services():
    return render_template("services.html", title="services")

@app.route('/quote')
def quote():
    return render_template("quote.html", title="quote")


if __name__ == "__main__":
    app.run(debug=True)