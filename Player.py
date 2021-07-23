import datetime as dt
import csv

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

        totalTime = 0
        for login, logout in zip(self.logins, self.logouts):
            totalTime += (logout[1] - login[1]).total_seconds()

        return totalTime

    def exportLogins(self, filename):
        if len(self.logouts) > len(self.logins):
            self.logouts = self.logouts[1:]

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Login Time'] + ['Logout Time'])
            for login, logout in zip(self.logins, self.logouts):
                loginText = login[1].strftime("%m/%d/%y %I:%M:%S %p")
                logoutText = logout[1].strftime("%m/%d/%y %I:%M:%S %p")
                csvwriter.writerow([loginText] + [logoutText])
