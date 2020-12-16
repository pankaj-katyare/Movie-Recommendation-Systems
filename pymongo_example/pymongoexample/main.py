from flask import Blueprint,render_template, redirect, url_for,request
from flask_pymongo import PyMongo 
mongo = PyMongo()
main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/adduser', methods=['POST'])
def adduser():
    user_collection = mongo.db.users
    #user_collection.insert_one({'name' : request.form.get('username')})
    

    Action = int(request.form['action'])
    Comedy = int(request.form["comedy"])
    Horror = int(request.form["horror"])
    Adventure = int(request.form["adventure"])
    Romance = int(request.form["romance"])
    Animation = int(request.form["animation"])

    user_collection.insert_one({'name' : request.form.get('username'),'Action' : Action , 'Comedy' : Comedy, 'Horror': Horror, 'Adventure' : Adventure, 'Romance' : Romance , 'Animation' : Animation  })

    return redirect(url_for('main.index'))

