# coding=utf-8

# This script is intended to be used with EventScripts on a Team Fortress 2 server, or possibly on other Source games. The script listens for team change events and moves players to the Mumble chatroom corresponding to the team they are playing on at the moment.

import es
from playerlib import getPlayerList
from subprocess import call
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

team_names = {2: 'RED',
              3: 'BLU'}

# Called when this script is loaded. Move all players.
def load():
    for player in getPlayerList():
        move_player(player.name, player.team)

# Called when a player changes teams. Move that player.
def player_team(event_var):
    move_player(event_var['es_username'], int(event_var['team']))

# Move player to the specified chatroom. The Ice library used to control the Mumble server is not available here in Python 2.5.1, so we call an external command.
def move_player(name, team):
    if team in team_names:
        call(['./move_user.py', name, team_names[team]])
