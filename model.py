from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey



db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(24), unique=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    

class Player(db.Model):

    __tablename__ = "player"

    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    player_name = db.Column(db.String(64), nullable=False)
    birthdate = db.Column(db.String(64))
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    attribute_date = db.Column(db.DateTime)
    overall_rating = db.Column(db.Integer, nullable=False)
    potential = db.Column(db.Integer, nullable=False)
    preferred_foot = db.Column(db.String(20), nullable=False)
    attacking_work_rate = db.Column(db.String(20), nullable=True)
    defensive_work_rate = db.Column(db.String(20), nullable=True)
    crossing = db.Column(db.Integer, nullable=True)
    finishing = db.Column(db.Integer, nullable=True)
    heading_accuracy = db.Column(db.Integer, nullable=True)
    short_passing = db.Column(db.Integer, nullable=True)
    long_passing = db.Column(db.Integer, nullable=True)
    volleys = db.Column(db.Integer, nullable=True)
    dribbling = db.Column(db.Integer, nullable=True)
    curve = db.Column(db.Integer, nullable=True)
    free_kick_accuracy = db.Column(db.Integer, nullable=True)
    ball_control = db.Column(db.Integer, nullable=True)
    acceleration = db.Column(db.Integer, nullable=True)
    sprint_speed = db.Column(db.Integer, nullable=True)
    agility = db.Column(db.Integer, nullable=True)
    reactions = db.Column(db.Integer, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    shot_power = db.Column(db.Integer, nullable=True)
    jumping = db.Column(db.Integer, nullable=True)
    stamina = db.Column(db.Integer, nullable=True)
    strength = db.Column(db.Integer, nullable=True)
    long_shots = db.Column(db.Integer, nullable=True)
    aggression = db.Column(db.Integer, nullable=True)
    interceptions = db.Column(db.Integer, nullable=True)
    positioning = db.Column(db.Integer, nullable=True)
    vision = db.Column(db.Integer, nullable=True)
    penalties = db.Column(db.Integer, nullable=True)
    marking = db.Column(db.Integer, nullable=True)
    standing_tackle = db.Column(db.Integer, nullable=True)
    sliding_tackle = db.Column(db.Integer, nullable=True)
    gk_diving = db.Column(db.Integer, nullable=True)
    gk_handling = db.Column(db.Integer, nullable=True)
    gk_kicking = db.Column(db.Integer, nullable=True)
    gk_positioning = db.Column(db.Integer, nullable=True)
    gk_reflexes = db.Column(db.Integer, nullable=True)

class Country(db.Model):

    __tablename__ = "country"

    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country_name = db.Column(db.String(64), nullable = False)

class League(db.Model):

    __tablename__ = "league"

    league_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country_id = db.Column(db.Integer, ForeignKey('country.country_id'))
    league_name = db.Column(db.String(65), nullable = False)

class Match(db.Model):

    __tablename__ = "match"

    match_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country_id = db.Column(db.Integer, ForeignKey('country.country_id'))
    league_id = db.Column(db.Integer, ForeignKey('league.league_id'))
    season = db.Column(db.String(64), nullable=True)
    stage = db.Column(db.String(64), nullable=True) 
    date = db.Column(db.String(64), nullable=True) 
    match_api_id = db.Column(db.Integer, nullable=True) 
    home_team_api_id = db.Column(db.Integer, nullable=True)
    away_team_api_id= db.Column(db.Integer, nullable=True)

class Team(db.Model):

    __tablename__ = "team"

    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_long_name = db.Column(db.String(64), nullable=False)
    team_short_name = db.Column(db.String(10), nullable=False)
    buildUpPlaySpeed = db.Column(db.Integer, nullable=True)
    buildUpPlaySpeedClass = db.Column(db.String(64), nullable=True)
    buildUpPlayDribblingClass= db.Column(db.String(64), nullable=True)
    buildUpPlayPassing= db.Column(db.Integer, nullable=True)
    buildUpPlayPassingClass= db.Column(db.String(64), nullable=True)
    buildUpPlayPositioningClass= db.Column(db.String(64), nullable=True)
    chanceCreationPassing= db.Column(db.Integer, nullable=True)
    chanceCreationPassingClass= db.Column(db.String(64), nullable=True)
    chanceCreationCrossing= db.Column(db.Integer, nullable=True)
    chanceCreationCrossingClass= db.Column(db.String(64), nullable=True)
    chanceCreationShooting= db.Column(db.Integer, nullable=True)
    chanceCreationShootingClass= db.Column(db.String(64), nullable=True)
    chanceCreationPositioningClass= db.Column(db.String(64), nullable=True)
    defencePressure= db.Column(db.Integer, nullable=True)
    defencePressureClass= db.Column(db.String(64), nullable=True)
    defenceAggression= db.Column(db.Integer, nullable=True)
    defenceAggressionClass= db.Column(db.String(64), nullable=True)
    defenceTeamWidth= db.Column(db.Integer, nullable=True)
    defenceTeamWidthClass= db.Column(db.String(64), nullable=True)
    defenceDefenderLineClass= db.Column(db.String(64), nullable=True)


class User_team(db.Model):

    __tablename__ = "user_team"

    user_team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))

    


class User_player(db.Model):
    
    __tablename__ = "user_player"

    user_player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))


def connect_to_db(app):
        # As a convenience, if we run this module interactively, it will leave
        # you in a state of being able to work with the database directly.
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///soccer_data_2'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.app = app
        db.init_app(app)

if __name__ == "__main__":
    from functions import app
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")
