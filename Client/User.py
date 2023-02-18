from Encrypt import *

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

def GetBalance():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((NetInfo.Host, NetInfo.Port))
        s.send(bytes(str("BAL:" + UserInfo.Name), 'utf-8'))
        InData = int(s.recv(1024))
        
    return InData     

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

    NetInfo.MainSocket.connect((NetInfo.Host, NetInfo.Port))
    NetInfo.MainSocket.send(bytes(str("ADD:" + Encrypt(UserInfo.Name)), 'utf-8'))

    NetInfo.MainSocket.close()    
    NetInfo.Restart()

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