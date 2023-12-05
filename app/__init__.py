from flask import Flask, render_template, request, redirect
from .Classes import Register,Gameadd,Adminlogin,Login
from flask_sqlalchemy import  SQLAlchemy
from  flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user,logout_user,current_user,login_required
from datetime  import datetime
from flask_caching import Cache

app= Flask(__name__)
app.config["SECRET_KEY"]="123"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data1.db'

cache = Cache(config={"CACHE_TYPE": 'SimpleCache',
                                        "CACHE_DEFAULT_TIMEOUT":300})

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login=LoginManager(app)
login.login_view="login"

class Userlist(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    password = db.Column(db.Integer, db.ForeignKey('user1.id'))
    age= db.Column(db.Integer, db.ForeignKey('posts.id'))

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

@login.user_loader
def user_loader(id):
    return  Userlist.query.get(id)

@app.route("/registration", methods=["GET", "POST"])
def page_1():
    registration=Register()
    if login.validate_on_submit():
        password = registration.password.data
        name = registration.name.data
        age = registration.age.data
        user=Userlist(name=name,password=password,age=age)
        db.session.add(user)
        db.session.commit()
        return render_template("Registration.html",password=password,name=name,age=age,registration=registration)
    return render_template("Registration.html",registration=registration)

@app.route("/", methods=["GET", "POST"])
def page_post():
    games = Games.query.all()
    return render_template('Gamespage.html', games=games,user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loggingin = Login()
    if loggingin.validate_on_submit():
        username=loggingin.username.data
        password=loggingin.password.data
        user=Userlist.query.filter_by(name_=username).first()
        if  user is None or user.password != password:
            return redirect("/login")
        login_user(user, remember=loggingin.remember.data)
    return render_template("Login.html",loggingin=loggingin)

@app.route("/userlist", methods=["GET", "POST"])
def show_all_users():
    allusers = Userlist.query.all()
    return render_template("Userlist.html", allusers=allusers)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
