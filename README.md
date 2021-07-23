# MCLogReader
This is a program meant to read the server logs of minecraft to find the login and logout times of every player.

This was created by David Rosenstein to find the total hours played by everyone on a Minecraft server.

How to use:
Edit the start of main.py with the names of the files that you want to look through. 
Then if you just run main.py you will find to total time played by every player on the server. 
If you want to export the times a player was online the server, import the python file and then run <player object>.exportLogins(<name of file>).
Make sure the logs you are looking at are in the same folder as the python files, as well as named after the date (as they are defaulted to)
