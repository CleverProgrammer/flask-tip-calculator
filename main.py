from flask import Flask, render_template, request, make_response, session
from replit import db
import requests

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

db['users'] = []
db['last_dog'] = ''

# leaderboard

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  if request.method == 'POST':
    user_name = request.form['user_name']
    print(f"Username 👉 {user_name}")
    db['users'].append({'user_name': user_name})
    session['user'] = user_name
    get_user = [user for user in db['users'] if user['user_name'] == user_name]
    resp = make_response(render_template('index.html', 
                                         dog_image=db['last_dog'],
                                         logged_in_user = user_name,
                                         session=session,
                                         dogs_generated=db['dog_images_generated']))
    resp.set_cookie('user_name', user_name)
    return resp
    
 
  db['dog_images_generated'] = db.get('dog_images_generated', 0) + 1
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  db['last_dog'] = data['message']
  print(request.cookies.get('user_name'))
  return render_template('index.html', 
                         dog_image=data['message'], 
                         logged_in_user = request.cookies.get('user_name'),
                         session=session,
                         dogs_generated=db['dog_images_generated'])
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81)