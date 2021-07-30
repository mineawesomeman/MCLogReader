# MCLogReader
This is a program meant to read the server logs of minecraft to find the login and logout times of every player.
(this file is much easier to read raw)

This was created by David Rosenstein to find the total hours played by everyone on a Minecraft server.

How to use:
First, put all of the logs into one folder. Make sure all the logs follow the default naming format (YYYY-MM-DD-#.log)
Then, import MCLogReader and run init(folder location). ie: MCLogReader.init("C:/Users/daraw/PycharmProjects/mcLogReader/logs/")
(note: you NEED the last slash at the end of the file path!)
Once imported, you can then use findTotalTimePlayed() to find the total time spent on your server.
To find the individual time played of each player you first need to find the player object using the players dict.
ie: MCLogReader.players["Mineawesome"]
Once you have the player object, you can run the following methods on them:
calculateTimeOnline() to find the total time that player played. Returns a deltaTime
exportLogins(filename) to export the login and logout times of the player. filename is the name of the file you want to export to


I currently have no plans to continue this project, and it is complete in my eyes, however if people find enough uses for this and would like more, I may revisit it.
