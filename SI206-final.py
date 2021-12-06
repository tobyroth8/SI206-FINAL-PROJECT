import html
import sqlite3
import json
from bs4 import BeautifulSoup
import requests
import os


def getStatesWithTeams():
    requestURL = "https://worldpopulationreview.com/state-rankings/nba-teams-by-state"
    master = []
    resp = requests.get(requestURL)
    soup = BeautifulSoup(resp.content, 'html.parser')
    soup.find_all('tr' , class_='jsx-2636433790')
    statename = soup.find_all( 'a', 'td')
    for var in statename.text:
        master.append(var)
    return master

getStatesWithTeams()