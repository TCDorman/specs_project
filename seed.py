from unittest.util import _count_diff_all_purpose
from sqlalchemy import insert
from model import Player, League, Match, Team, Country, connect_to_db, db
from server import app

def load_players():
    counter = 0
    for line in open('csvs/players_master2.csv'):
        mylist = line[:-1]
        player_id,player_name,birthdate,height,weight,overall_rating,potential,preferred_foot,attacking_work_rate,defensive_work_rate,crossing,finishing,heading_accuracy,short_passing,long_passing,volleys,dribbling,curve,free_kick_accuracy,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes = mylist.split(",")
        player = Player(player_id=int(player_id), player_name=player_name, birthdate=birthdate, 
        height=height, weight=weight , overall_rating=int(overall_rating), potential=int(potential) , 
        preferred_foot=preferred_foot , attacking_work_rate=attacking_work_rate , 
        defensive_work_rate=defensive_work_rate , crossing=int(crossing) , finishing=int(finishing) , 
        heading_accuracy=int(heading_accuracy) , short_passing=int(short_passing) , 
        long_passing=int(long_passing), volleys=int(volleys) , dribbling=int(dribbling) , 
        curve=int(curve) , free_kick_accuracy=int(free_kick_accuracy) , ball_control=int(ball_control) , 
        acceleration=int(acceleration) , sprint_speed=int(sprint_speed) , agility=int(agility) , 
        reactions=int(reactions) , balance=int(balance) , shot_power=int(shot_power) , 
        jumping=int(jumping) , stamina=int(stamina) , strength=int(strength) , long_shots=int(long_shots) , 
        aggression=int(aggression) , interceptions=int(interceptions), positioning=int(positioning) , 
        vision=int(vision) , penalties=int(penalties), marking=int(marking) , 
        standing_tackle=int(standing_tackle) , sliding_tackle=int(sliding_tackle) , gk_diving=int(gk_diving) , 
        gk_handling=int(gk_handling) , gk_kicking=int(gk_kicking) , gk_positioning=int(gk_positioning) , 
        gk_reflexes=int(gk_reflexes))
        db.session.add(player)
        if counter % 100 == 0:
            print(counter)
        counter += 1
        
    db.session.commit()
    print("done")

def load_country():
    counter = 0
    for line in open('csvs/Country.csv'):
        mylist = line[0:-1]
        country_id, country_name = mylist.split(",")
        country = Country(country_id=int(country_id), country_name=country_name)
        db.session.add(country)
        if counter % 100 == 0:
            print(counter)
        counter += 1
    db.session.commit()
    print("done")

def load_league():
    counter = 0
    for line in open('csvs/League.csv'):
        mylist = line[:-1]
        league_id, country_id, league_name = mylist.split(",")
        league = League(league_id=int(league_id), country_id=country_id, league_name=league_name)
        db.session.add(league)
        if counter % 100 == 0:
            print(counter)
        counter += 1

    db.session.commit()
    print("done")


def load_match():
    counter = 0
    for line in open('csvs/clean_match.csv'):
        mylist = line[:-1]
        match_id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, away_team_api_id = mylist.split(",")
        match = Match(match_id=int(match_id), country_id=country_id, league_id=league_id, season=season, stage=stage, date=date, match_api_id=int(match_api_id), home_team_api_id=int(home_team_api_id), away_team_api_id=int(away_team_api_id))
        db.session.add(match)
        if counter % 100 == 0:
            print(counter)
        counter += 1
    db.session.commit()
    print("done")

def load_teams():
    counter = 0
    for line in open('csvs/team_master.csv'):
        mylist = line[:-1]
        print(mylist)
        team_id,team_long_name,team_short_name,buildUpPlaySpeed,buildUpPlaySpeedClass,buildUpPlayDribblingClass,buildUpPlayPassing,buildUpPlayPassingClass,buildUpPlayPositioningClass,chanceCreationPassing,chanceCreationPassingClass,chanceCreationCrossing,chanceCreationCrossingClass,chanceCreationShooting,chanceCreationShootingClass,chanceCreationPositioningClass,defencePressure,defencePressureClass,defenceAggression,defenceAggressionClass,defenceTeamWidth,defenceTeamWidthClass,defenceDefenderLineClass = mylist.split(",")
        team = Team(team_id=int(team_id),team_long_name=team_long_name,team_short_name=team_short_name,buildUpPlaySpeed=int(buildUpPlaySpeed),buildUpPlaySpeedClass=buildUpPlaySpeedClass,buildUpPlayDribblingClass=buildUpPlayDribblingClass,buildUpPlayPassing=int(buildUpPlayPassing),buildUpPlayPassingClass=buildUpPlayPassingClass,buildUpPlayPositioningClass=buildUpPlayPositioningClass,chanceCreationPassing=int(chanceCreationPassing),chanceCreationPassingClass=chanceCreationPassingClass,chanceCreationCrossing=int(chanceCreationCrossing),chanceCreationCrossingClass=chanceCreationCrossingClass,chanceCreationShooting=int(chanceCreationShooting),chanceCreationShootingClass=chanceCreationShootingClass,chanceCreationPositioningClass=chanceCreationPositioningClass,defencePressure=int(defencePressure),defencePressureClass=defencePressureClass,defenceAggression=int(defenceAggression),defenceAggressionClass=defenceAggressionClass,defenceTeamWidth=int(defenceTeamWidth),defenceTeamWidthClass=defenceTeamWidthClass,defenceDefenderLineClass=defenceDefenderLineClass) 
        db.session.add(team)
        if counter % 100 == 0:
            print(counter)
        counter += 1
    db.session.commit()
    print("done")


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()