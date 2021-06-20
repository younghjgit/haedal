from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def hello():
    return "2018113534 전자공학부 정영훈"

@app.route("/me/")
def aboutme():
    menu = ["chicken.jpg", "dog.jpg", "knu.jpg"]
    pickme = random.choice(menu)
    return render_template('index.html', img=pickme)

if __name__ == "__main__":
    app.run(debug=True)