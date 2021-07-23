import datetime as dt
import re
import Player

running = True
files = ['2021-07-13-1.log', '2021-07-14-1.log', '2021-07-15-1.log', '2021-07-16-1.log', '2021-07-16-2.log',
         '2021-07-16-3.log', '2021-07-16-4.log', '2021-07-17-1.log', '2021-07-18-1.log', '2021-07-19-1.log',
         '2021-07-20-1.log', '2021-07-21-1.log', '2021-07-22-1.log']
allLogins = []
allLogouts = []
players = {}

for file in files:
    todayLogins = []
    todayLogouts = []
    with open(file, "r", encoding='utf-8') as log:
        text = log.read()
        todayLogins.append(re.findall(r"\[(\d\d):(\d\d):(\d\d)\] \[.*\]: (.*)\[.*\] logged in with entity id .*", text))
        todayLogouts.append(re.findall(r"\[(\d\d):(\d\d):(\d\d)\] \[.*\]: (.*) left the game", text))
        log.close()

    date = dt.date(int(file[0:4]), int(file[5:7]), int(file[8:10]))
    for login in todayLogins[0]:
        time = dt.time(int(login[0]), int(login[1]), int(login[2]))
        playerName = login[3]
        dati = dt.datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)
        newLogin = (playerName, dati)
        allLogins.append(newLogin)
        if not players.__contains__(playerName):
            players[playerName] = Player.Player(playerName)
        players[playerName].addLogin(newLogin)

    for logout in todayLogouts[0]:
        time = dt.time(int(logout[0]), int(logout[1]), int(logout[2]))
        playerName = logout[3]
        dati = dt.datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)
        newLogout = (playerName, dati)
        allLogouts.append(newLogout)
        if not players.__contains__(playerName):
            players[playerName] = Player.Player(playerName)
        players[playerName].addLogout(newLogout)

totalTime = 0
for player in players.values():
    totalTime += player.calculateTimeOnline()
    print(player.name, player.calculateTimeOnline()/3600)

print("Total time", totalTime/3600)
