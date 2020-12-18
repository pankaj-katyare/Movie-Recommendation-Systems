#to run this code change URI in .env file
#run command : pip install flask flask-pymongo python-dotenv
#run command : flask run

from flask import Blueprint,render_template,redirect,url_for,request,session,Flask
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def welcome():   
    return render_template('index.html')

@main.route('/home', methods=['POST'])
def home():
    if 'username' in session:       
        
        #we are creating a session and that session name=username
        usernamenow = session['username']       
        #extraction of HTML name attributes from the users are stored
        Action = int(request.form['action'])     
        Comedy = int(request.form["comedy"])
        Horror = int(request.form["horror"])
        Adventure = int(request.form["adventure"])
        Romance = int(request.form["romance"])
        Animation = int(request.form["animation"])

        #appending user preferences with its username and password in mongoDB
        preference = { "Action":Action, "Comedy":Comedy, "Horror":Horror, "Adventure":Adventure, "Romance":Romance,"Animation":Animation}

        return 'hello'

#validates username and password
@main.route('/login', methods=['POST'])
def login():
    
    return 'Invalid username/password combination'

#registration of new user
@main.route('/register', methods=['POST', 'GET'])
def register(username):
    if request.method == 'POST':
        
        password = request.form['pass']
        hashpass = generate_password_hash(password)

        credentials = {"name" : name , "password" : hashpass}
        datastore.save_credentials(credentials)
            #users.insert({'name' : request.form['username'], 'password' : hashpass})
        session['username'] = request.form['username']
            #after user registers he is taken to the preference page
        
    return render_template('recommend.html')

@main.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
