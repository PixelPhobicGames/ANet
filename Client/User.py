from Encrypt import *
from Etc import *

import socket

def PullAddress():
    ConfFile = open("AppData/Server/Address.conf", "r+")
    Address = ConfFile.read()
    ConfFile.close
    return Address

class NetInfo:
    Host = PullAddress()
    Port = 12345  

    def Restart():
        Host = PullAddress()
        Port = 12345 

def Fix(Text):
    return Text[2:len(Text)-1]

def CheckServer():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as MainSocket:
            MainSocket.connect((NetInfo.Host, NetInfo.Port))
            MainSocket.send(bytes(str("CHECK:"), 'utf-8'))
            InData = MainSocket.recv(1024)
            if (Fix(str(InData)) == "Here"):
                return True
            else:
                return False
    except:
        return False

def GetBalance():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as MainSocket:
            MainSocket.connect((NetInfo.Host, NetInfo.Port))
            MainSocket.send(bytes(str("BAL:" + UserInfo.Name), 'utf-8'))
            InData = int(MainSocket.recv(1024))
            
        return InData    
    except:
        return "Error"

class UserInfo:
    Name = ''
    Number = ''
    Password = ''
    Address = ''
    Balance = 0

def GenerateIDInfo():
    ConfFile = open("AppData/User/User.conf", "w+")
    ConfFile.write(str(Encrypt(UserInfo.Name) + ":" + Encrypt(UserInfo.Number)  + ":" + Encrypt(UserInfo.Password)  + ":" + Encrypt(UserInfo.Address)))
    ConfFile.close

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as MainSocket:
        MainSocket.connect((NetInfo.Host, NetInfo.Port))
        MainSocket.send(bytes(str("ADD:" + Encrypt(UserInfo.Name)), 'utf-8'))

def PullID():

    ConfFile = open("AppData/User/User.conf", "r")
    FileData = ConfFile.read()

    Info = FileData.split(":")

    if (len(FileData) != 0):

        UserInfo.Name = Info[0]
        UserInfo.Number = Info[1]
        UserInfo.Password = Info[2]
        UserInfo.Address = Info[3]
        ConfFile.close

        return 1
    else:
        return 0