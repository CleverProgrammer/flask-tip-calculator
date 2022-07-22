# TODO: leaderboard

from flask import Flask, render_template, request, session
from replit import db
import requests

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEYY'

app.config["SESSION_COOKIE_SAMESITE"] = 'None'
app.config["SESSION_COOKIE_SECURE"] = True

if 'users' not in db:
  db['users'] = []

if 'dogs_generated' not in db:
  db['dogs_generated'] = 0
  
db['last_dog'] = ''

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  
  if request.method == 'POST':
    user_name = request.form['user_name']
    user = create_or_update_user(user_name)
    # user = get_user_from_database(user_name)
    session['user'] = user_name
    session['logins'] = user['logins']
  else:
    user = None
    
  
  return render_template('index.html', 
                         dogs_generated=db['dog_images_generated'],
                         user=user
                        )

@app.route('/get_dog')
def get_dog():
  if session['user']:
    user = get_user_from_database(session['user'])
    user['dogs_generated'] = user.get('dogs_generated', 0) + 1
  
  db['dog_images_generated'] = db.get('dog_images_generated', 0) + 1
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  db['last_dog'] = data['message']
  dogs_generated=db['dog_images_generated']
  dog_image=data['message']
    
  return render_template('index.html', 
                         dogs_generated=db['dog_images_generated'],
                         dog_image=data['message'],
                         user=user
                        )

@app.route('/logout')
def logout():
  session['user'] = None
  return render_template('index.html', dogs_generated=db['dog_images_generated'])


'''
Create new user if they don't exist
>>> create_or_update_user(None, 'david')
ObservedDict(value={'user_name': 'david', 'logins': 1, 'dogs_generated': 0})

Update existing user
>>> create_or_update_user(ObservedDict(value={'user_name': 'kevin', 'logins': 3, 'dogs_generated': 0}), 'david')
ObservedDict(value={'user_name': 'david', 'logins': 3, 'dogs_generated': 0})
'''
def create_or_update_user(user_name):
  user = get_user_from_database(user_name)
  
  if user:
      user['logins'] += 1
  else:
    print('errors are happening here.')
    db['users'].append({
      'user_name': user_name,
      'logins': 1,
      'dogs_generated': 0,
    })
    user = get_user_from_database(user_name)

  return user

# abstract this away from users
'''
If a user exists...
>>> get_user_from_database('david')
ObservedDict(value={'user_name': 'david', 'logins': 15, 'dogs_generated': 0})

If no user...
>>> get_user_from_database('kevin')
None
'''
def get_user_from_database(user_name):
  user = [user for user in db['users'] if user['user_name'] == user_name]
  return user[0] if user else None

  

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81)