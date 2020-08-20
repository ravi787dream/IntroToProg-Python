# ------------------------------------------ #
# Title: Assignment05
# Description: Working with Dictionaries and Files
#              When the program start, load each "row" of data
#              in "Todolist.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list 'table'
# Change log (Who, When, What)
# Ravi S/ 8-18/Create a Script
# ------------------------------------------ #


# Declare my variables
strChoice = '' # User input
lstTable = []
dicRow = {} # list of data
strFile = 'TestTODO.txt' # data storage file
objFile = None # file handle
strMenu = "" # user options.
strChoice = "" # A capture use options.

 # --------------- Dat

while (True):
    print("Select Your Option or type 'exit' ")
    strChoice = input(" Type [A] to add to todo list or [D] for display or Type [L] for full list: ")
    if (strChoice.lower() == 'exit'): break
    elif(strChoice.lower() == 'a'):
        objFile = open(strFile, "a")
        strTask=input ("add your task : ")
        print(str(strTask))
        strPri= input ( " add your prior : ")
        print(str(strPri))
        dicRow = {"Task" : strTask , "Prior" : strPri}
        lstTable.append(dicRow)
        print ( "Task "  +  " Priority")
        print(dicRow)
        objFile.write(dicRow["Task"] + " | " + dicRow["Prior"] + '\n')
        objFile.close()
    elif (strChoice.lower()== 'd'):
        print(lstTable)

    elif(strChoice.lower() == 'l'):
        print("Task" + "|" + "Priority ")
        objFile = open(strFile, 'r')
        for row in objFile:
            lstRow = row.split('|')
            print(lstRow[0] + "|"+ lstRow[1])
