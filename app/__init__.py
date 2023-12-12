from flask import Flask, render_template, request, redirect
from .Classes import Register,Login,Login,adminLogincheck,addgame
from flask_sqlalchemy import  SQLAlchemy
from  flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user,logout_user,current_user,login_required
from datetime  import datetime
from flask_caching import Cache

basket=[]

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
    password = db.Column(db.String,nullable=False)
    age = db.Column(db.Integer,nullable=False)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    path = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

@login.user_loader
def user_loader(id):
    return  Userlist.query.get(id)

@app.route("/registration", methods=["GET", "POST"])
def page_1():
    registration =Register()
    if registration.validate_on_submit():
        password = registration.password.data
        name = registration.name.data
        age = registration.age.data
        user =Userlist(name=name,password=password,age=age)
        db.session.add(user)
        db.session.commit()
        return render_template("Registration.html",password=password,name=name,age=age,registration=registration)
    return render_template("Registration.html",registration=registration)

@app.route("/", methods=["GET", "POST"])
def page_post():
    games = Games.query.all()
    return render_template('Gamespage.html', games=games,user=current_user)

@app.route('/addgame', methods=['GET', 'POST'])
@login_required
def addgame():
    adminlogin = adminLogincheck()
    if adminlogin.validate_on_submit():
        username=adminlogin.username.data
        password=adminlogin.password.data
        admin=Userlist.query.filter_by(name=username).first()
        if  admin is None or admin.name != username or password != 1234567890:
            return redirect("/addgame")
        else:
            Create = addgame()
            if Create.validate_on_submit():
                Name =addgame.name.data
                Description = addgame.description.data
                Price = addgame.price.data
                Path = addgame.image.data
                game = Games(name=Name,description=Description,price=Price,path=Path)
                db.session.add(game)
                db.session.commit()
            return render_template("SECAddgame.html",Create=Create)
    return render_template("Addgame.html",adminlogin=adminlogin)

@app.route("/userlist", methods=["GET", "POST"])
@login_required
def show_all_users():
    allusers = Userlist.query.all()
    return render_template("Userlist.html", allusers=allusers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loggingin = Login()
    if loggingin.validate_on_submit():
        username=loggingin.username.data
        password=loggingin.password.data
        user=Userlist.query.filter_by(name=username).first()
        if  user is None or user.password != password:
            return redirect("/login")
        login_user(user, remember=loggingin.remember.data)
    return render_template("Login.html",loggingin=loggingin)

@app.route('/game/<int:id>', methods=['GET', 'POST'])
@login_required
def add(id):
    game = Games.query.get(id)
    data=game.name
    if data in basket:
        return redirect('/')
    else:
        basket.append(data)
        return redirect('/')

@app.route('/basket>', methods=['GET', 'POST'])
@login_required
def basket():
    items=basket
    return render_template("Basket.html", items=items)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/clear")
def clear():
    basket=[]
    return redirect("/basket")

