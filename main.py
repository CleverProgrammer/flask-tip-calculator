from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"


@app.route('/increase_people')
def increase_people():
    print('increase')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81)
