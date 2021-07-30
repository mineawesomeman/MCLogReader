import datetime as dt
import re
import csv
from glob import glob


class Player:
    name = ''
    logins = None
    logouts = None

    def __init__(self, name):
        self.name = name
        self.logins = []
        self.logouts = []

    def addLogin(self, login):
        self.logins.append(login)

    def addLogout(self, logout):
        self.logouts.append(logout)

    def calculateTimeOnline(self):
        if len(self.logouts) > len(self.logins):
            self.logouts = self.logouts[1:]

        totalTime = dt.timedelta(0)
        for login, logout in zip(self.logins, self.logouts):
            totalTime = totalTime + (logout[1] - login[1])

        return totalTime

    def exportLogins(self, filename):
        if len(self.logouts) > len(self.logins):
            self.logouts = self.logouts[1:]

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Login Time'] + ['Logout Time'])
            for login, logouts in zip(self.logins, self.logouts):
                loginText = login[1].strftime("%m/%d/%y %I:%M:%S %p")
                logoutText = logouts[1].strftime("%m/%d/%y %I:%M:%S %p")
                csvwriter.writerow([loginText] + [logoutText])


allLogins = []
allLogouts = []
players = {}


def init(loc):
    files = glob(loc + "*.log")

    for file in files:
        todayLogins = []
        todayLogouts = []
        with open(file, "r", encoding='utf-8') as log:
            text = log.read()
            todayLogins.append(
                re.findall(r"\[(\d\d):(\d\d):(\d\d)\] \[.*\]: (.*)\[.*\] logged in with entity id .*", text))
            todayLogouts.append(re.findall(r"\[(\d\d):(\d\d):(\d\d)\] \[.*\]: (.*) left the game", text))
            fileInfo = re.findall(r"(\d{4})-(\d{2})-(\d{2})-\d*.log", log.name)[0]
            log.close()

        date = dt.date(int(fileInfo[0]), int(fileInfo[1]), int(fileInfo[2]))
        for this_login in todayLogins[0]:
            time = dt.time(int(this_login[0]), int(this_login[1]), int(this_login[2]))
            playerName = this_login[3]
            dati = dt.datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)
            newLogin = (playerName, dati)
            allLogins.append(newLogin)
            if not players.__contains__(playerName):
                players[playerName] = Player(playerName)
            players[playerName].addLogin(newLogin)

        for this_logout in todayLogouts[0]:
            time = dt.time(int(this_logout[0]), int(this_logout[1]), int(this_logout[2]))
            playerName = this_logout[3]
            dati = dt.datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)
            newLogout = (playerName, dati)
            allLogouts.append(newLogout)
            if not players.__contains__(playerName):
                players[playerName] = Player(playerName)
            players[playerName].addLogout(newLogout)


def findTotalTimePlayed():
    totalTime = dt.timedelta(0)
    for player in players.values():
        totalTime += player.calculateTimeOnline()

    return totalTime
