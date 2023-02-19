
import socket
import os

from Encrypt import *
from Data import *


MainSocket = socket.socket()  
MainSocket.bind((Host, Port))
MainSocket.listen()

while True:
    Connection, Address = MainSocket.accept()

    print(f"Conntion From {Address}")

    RawCommand = str(Connection.recv(1024))
    ParsedCommand = RawCommand[2:len(RawCommand) - 1]
    
    print("Server Command: " , ParsedCommand)

    if (ParsedCommand.split(":")[0] == "BAL"):
        if (CheckItem(ServerBalanceInfo , Fix(RawCommand.split(":")[1]))):
            data = bytes(ServerBalanceInfo[Fix(RawCommand.split(":")[1])], 'utf-8')
            Connection.send(data)
            Connection.close()
            MainSocket.listen()
        else:
            Connection.send(bytes("0", 'utf-8'))
            ServerBalanceInfo.update({Fix(RawCommand.split(":")[1]):"0"})
            Connection.close()
            MainSocket = socket.socket()  
    if (ParsedCommand.split(":")[0] == "CHECK"):
        data = bytes("Here", 'utf-8')
        Connection.send(data)
        Connection.close()
        MainSocket.listen()

    if (ParsedCommand.split(":")[0] == "ADD"):
        ServerBalanceInfo.update({Fix(RawCommand.split(":")[1]):"0"})
        Connection.close()
        MainSocket.listen()

    if (ParsedCommand.split(":")[0] == "ADDBAL"):
        
        ServerBalanceInfo.update({RawCommand.split(":")[1]:Fix(RawCommand.split(":")[2])})

        Connection.close()
        MainSocket.listen()

    if (ParsedCommand.split(":")[0] == "ORD"):

        Name = RawCommand.split(":")[1]
        Number = RawCommand.split(":")[3]
        ID = RawCommand.split(":")[4]
        Address = RawCommand.split(":")[2]
        Directions = RawCommand.split(":")[6]

        FileName = str("Orders/Order" + str(OrderCounter) + ".ord")

        os.system(str('echo "" << '+ FileName))
        OrderFile = open(FileName, "w")

        OrderFile.write(str("Order: Name - " + Name + " - Number - " + Number  + " - ID - " + ID  + " - Address - " + Address + " - Directions - " + Fix(Directions) +"\n"))
        OrderFile.close

        OrderCost = int(str(RawCommand.split(":")[5]))
        Balance = int(ServerBalanceInfo[RawCommand.split(":")[1]])

        ServerBalanceInfo.update({RawCommand.split(":")[1] : str(Balance - OrderCost)})

        OrderCounter += 1
    
        Connection.close()
        MainSocket.listen()
