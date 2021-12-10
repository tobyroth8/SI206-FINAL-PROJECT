import html
import sqlite3
import json
from bs4 import BeautifulSoup
import requests
import os
#Names: Zack, Toby, Luc

def getStatesWithTeams():
    requestURL = "https://worldpopulationreview.com/us-cities"
    master = []
    master1 = []
    resp = requests.get(requestURL)
    soup = BeautifulSoup(resp.content, 'html.parser')
    statename = soup.find_all( 'tbody', class_ = 'jsx-2636433790')
    for var in statename:
        # x = var.find_all('a')
        # for variable in x:
        #     master.append(variable.text)
        y = var.find_all('td')
        for variable in y:
            master1.append(variable.text)
    print(master1)

getStatesWithTeams()

def getUSNBATeams():
    requestURL = "https://www.cbssports.com/nba/teams/"
    master = []
    resp = requests.get(requestURL)
    soup = BeautifulSoup(resp.content, 'html.parser')
    teamname1 = soup.find_all(class_ = "TeamName")
    for team in teamname1:
        x = team.find_all('a')
        for variable in x:
            master.append(variable.text)
    master.pop(4)
    print(master)

getStatesWithTeams()
getUSNBATeams()
