from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# background process happening without any refreshing
@app.route('/get_dog')
def get_dog():
    print("woof woof! 🐶")
    return "woof woof! 🐶"


@app.route('/increase_people')
def increase_people():
    print('increase')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81)
