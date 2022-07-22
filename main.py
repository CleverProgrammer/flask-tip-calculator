from flask import Flask, render_template, request, session
from replit import db
import requests

# tip calculator is GUCCI
# damnnn boiiIIiIIii my manNNnnNNnnNn
# yo, check out this app in a NEW BROWSER.
# open new window and play with it.
# user logins + conditional rendering and everything!
# ohshitttttt. aight imma fork and let's see

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEYY'

if 'users' not in db:
  db['users'] = []
  
db['last_dog'] = ''

# big feature: leaderboard
# number of logins for that user
# dogs generated for that user
def create_or_update_user(user):
  if user:
      print('this USER exists already! Welcome back!')
      print(user)
      user['logins'] += 1
  else:
    db['users'].append({
      'user_name': user_name,
      'logins': 1,
      'dogs_generated': 0,
    })
    print('NEW USER REGISTERED')

  # print(f"Username 👉 {user_name}")
  # print(f"user 👉 {user}")
  
  # print(f'appending new user... {user_name}')
  # print(db['users'])

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  if request.method == 'POST':
    user_name = request.form['user_name']
    user = next((user for user in db['users'] if user['user_name'] == user_name), None)
  
    create_or_update_user(user)
    session['user'] = user_name
    
    
 
  db['dog_images_generated'] = db.get('dog_images_generated', 0) + 1
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  data = response.json()
  db['last_dog'] = data['message']
  print(request.cookies.get('user_name'))
  return render_template('index.html', 
                         dog_image=data['message'], 
                         dogs_generated=db['dog_images_generated'])


@app.route('/logout')
def logout():
  session['user'] = None
  return render_template('index.html', dogs_generated=db['dog_images_generated'])

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81)