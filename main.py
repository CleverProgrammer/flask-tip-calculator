from flask import Flask, render_template
from replit import db
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    db['dog_images_generated'] = db.get('dog_images_generated', 0) + 1
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    return render_template('index.html', dog_image=data['message'], dogs_generated=db['dog_images_generated'])
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81)