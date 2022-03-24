from crypt import methods
from unicodedata import name
from django.shortcuts import render
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from model import Player, User, User_player, User_team, Team, League, Country, Match, UserMixin, db
from flask_bcrypt import Bcrypt
import os 
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
login_manager = LoginManager(app)

app.jinja_env.undefined = StrictUndefined


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/register', methods=['GET'])
def registration_form():
    """Show form for user signup"""
    
    return render_template("registration_page.html")

@app.route('/register_process', methods=['POST'])
def register_process():
    
    username = request.form['username']
    email = request.form['email']
    print(type(request.form['password']))
    hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

    user = User.query.filter_by(email=email).first()
    user1 = User.query.filter_by(username=username).first()
    print(user)
    if user != None:
        if user.email == email:
            flash(f"email {email} already in use, please try another email.")
        return redirect('/register')
            
    if user1 != None:
        if user1.username == username:
            flash(f"User {username} already exists please try another username")
        return redirect('/register')
        

    new_user = User(username=username, email=email, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()

    flash(f"User {username} has been created.")
    return render_template("/users")


@app.route('/login', methods=['GET'])
def login_form():
    """Show form for login"""
    league = League.query.all()
    return render_template("login.html", league=league)

@app.route('/login_process', methods=['GET','POST'])
def login_process():
    """Process Logins"""
    
    print("login started")
    email = request.form["email"]
    password = request.form["password"]
    print(email)
    print(password)
    
    user = User.query.filter_by(email=email).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return render_template("/users.html", user=user)
    else:
        flash('Login Unsuccessful. Please check credentials and try again.')
        return render_template("/login.html")
    # if not user:
    #     print('not user')
    #     flash("No such user")
    #     return redirect('login')

    # if user.password != password:
    #     print('password issue')
    #     flash("Incorrect password")
    #     return redirect("/login")

    # session["user_id"] = user.user_id
    # print('user session found')
    # flash("logged in")
    # return render_template("users.html", user=user)

@app.route('/users', methods=['GET'])
def get_fav_player():
    return render_template("users.html")


@app.route('/logout')
def logout():
    """ log out """
    del session["user_id"]
    flash("logged out")
    return redirect("/")

@app.route('/players')
def players():
    return render_template("players.html", player_list=[])

@app.route('/players_get', methods=['GET'])
def players_page():
    """Show players page"""
    args = request.args
    overall_rating = args.get('overall_rating')
    group_overall_query = Player.query.filter_by(overall_rating=int(overall_rating)).all()
    print(len(group_overall_query))
    return render_template("players.html", player_list=group_overall_query)

@app.route('/search_player_name', methods=['GET', 'POST'])
def search_player_name():

    player_name = request.form['player_name']
    player2_name = request.form['player2_name']
    print(type(player_name))
    print(player2_name)
    player_query = Player.query.filter_by(player_name=player_name).first()
    player2_query = Player.query.filter_by(player_name=player2_name).first()
    

    return render_template("selected_players.html", player=player_query, player2=player2_query)


@app.route('/search_player_name', methods=['GET'])
def webscraper():
    player_name = request.form['player_name']
    return player_name


@app.route('/teams', methods=['GET'])
def teams_page():
    """Show teams page"""
    league = League.query.all()
    return render_template("teams.html", league=league)

@app.route('/search_team_name', methods=['GET', 'POST'])
def search_team_name():
    team_name = request.form['team_name']
    team2_name = request.form['team2_name']
    print(team_name)
    print(team2_name)
    team = Team.query.filter_by(team_long_name=team_name).first()
    team2 = Team.query.filter_by(team_long_name=team2_name).first()
    return render_template("selected_teams.html", team=team, team2=team2)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///soccer_data_2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)
    bcrypt = Bcrypt(app)
    app.run(debug=True, port=8000)
