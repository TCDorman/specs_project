from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin

db = SQLAlchemy()



class User(db.Model, UserMixin):

    __tablename__ = "users"
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(24), unique=True)
    email = db.Column(db.String(64), nullable=False)
    def get_id(self):
           return (self.user_id)
    password = db.Column(db.String(64), nullable=False)

class Player(db.Model):

    def __init__(self, arg):
        self.arg = arg

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

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<Player player_id={self.player_id} overall_rating={self.overall_rating}>"

    
class Country(db.Model):

    __tablename__ = "country"

    country_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country_name = db.Column(db.String(64), nullable = False)

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<Country country_id={self.country_id} country_name={self.country_name}>"


class League(db.Model):

    __tablename__ = "league"

    league_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country_id = db.Column(db.Integer, ForeignKey('country.country_id'))
    league_name = db.Column(db.String(65), nullable = False)

    country = db.relationship("Country", backref=db.backref("league", order_by=league_id))

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<League league_id={self.league_id} league_name={self.league_name} country_id={self.country_id}>"


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

    country = db.relationship("Country", backref=db.backref("match", order_by=match_id))
    league = db.relationship("League", backref=db.backref("match", order_by=match_id))

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<Match match_id={self.match_id} season={self.season} date={self.date}>"


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

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<Team team_id={self.team_id} team_long_name={self.team_long_name} team_short_name={self.team_short_name}>"


class User_team(db.Model):

    __tablename__ = "user_team"

    user_team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))

    user = db.relationship("User", backref=db.backref("user_team", order_by=user_team_id))
    team = db.relationship("Team", backref=db.backref("user_team", order_by=user_team_id))

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<User_team user_team_id={self.user_team_id} user_id={self.user_id} team_id={self.team_id}>"

    
class User_player(db.Model):
    
    __tablename__ = "user_player"

    user_player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))

    user = db.relationship("User", backref=db.backref("user_player", order_by=user_player_id))
    player = db.relationship("Player", backref=db.backref("user_player", order_by=user_player_id))

    def __repr__(self):
        """Provide helpful representation when needed"""

        return f"<User_player user_player_id={self.user_player_id} user_id={self.user_id} player_id={self.player_id}>"


def connect_to_db(app):
        # As a convenience, if we run this module interactively, it will leave
        # you in a state of being able to work with the database directly.
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///soccer_data_2'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db.app = app
        db.init_app(app)

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")
