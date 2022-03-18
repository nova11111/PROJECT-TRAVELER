'''
Matthew Fulmer
Assignment: Fantastic Landscape
'''

from cmath import log
import random

#Commands of Program
Commands = ("walk",
            "end",
            "log")
#First Halves of Location Names
Locations_Partone = ("Xialtha",
                    "Saintsteel",
                    "Ecclesia",
                    "Hyperion",
                    "Azir",
                    "Valis")
#Second Halves of Location Names
Locations_Parttwo = ("Reliquary",
                    "Forest",
                    "Imperial Capital",
                    "Ruins",
                    "Village",
                    "Temple",
                    "Valley",
                    "Mountain",
                    "Island")
Locations_Log = []
#Code that Runs
#Opening Message
print("Greetings, Traveler!")
input()
#Loop Begins
loop_Continue = True
while loop_Continue == True:
#Ask for Commands
    User_Command = input("What will you do?")
    User_Command = User_Command.lower()
    if User_Command == "walk":
        Walk_IsRunning = True
        if Walk_IsRunning == True:
            Location_First = random.choice(Locations_Partone)
            Location_Second = random.choice(Locations_Parttwo)
            Walk_IsRunning = False
#Combine Halves to form Location Name
        Location_Name = Location_First + " " + Location_Second
        print("You Traveled to", Location_Name) 
        User_Command = ""
#results if Walk is Used
#Randomly Pick 1st and 2nd Half of Location Name      
#Print travel message
        if Location_Name in Locations_Log:
            print("You have already been here.")
#Check if Location is in log
        if Location_Name not in Locations_Log:
            Locations_Log.append(Location_Name)
    #Add to the log if it is not
#Print Message stating the location is old if it is
#go to start of loop
    if User_Command == "end":
        loop_Continue = False
        User_Command = ""
#Results if End is used
#end loop
#Results if Command log is used
    if User_Command == "log":
            print(Locations_Log)
            User_Command = ""
#print Log
    if User_Command not in Commands:
        continue
#Results if invalid command is used
print("Safe Travels!")
input()
#go to start of loop