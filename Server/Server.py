
import socket    


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)


ServerBalanceInfo = {'VDZM XLOV' : "165"}

class LocalKey:
    Key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

def Encrypt(Text):
    OutString = ''
    Counter = 0
    while (Counter != len(Text)):
        if (Text[Counter] == 'A' or Text[Counter] == 'a'):
            OutString += LocalKey.Key[0]
        if (Text[Counter] == 'B' or Text[Counter] == 'b'):
            OutString += LocalKey.Key[1]
        if (Text[Counter] == 'C' or Text[Counter] == 'c'):
            OutString += LocalKey.Key[2]
        if (Text[Counter] == 'D' or Text[Counter] == 'd'):
            OutString += LocalKey.Key[3]
        if (Text[Counter] == 'E' or Text[Counter] == 'e'):
            OutString += LocalKey.Key[4]
        if (Text[Counter] == 'F' or Text[Counter] == 'f'):
            OutString += LocalKey.Key[5]
        if (Text[Counter] == 'G' or Text[Counter] == 'g'):
            OutString += LocalKey.Key[6]
        if (Text[Counter] == 'H' or Text[Counter] == 'h'):
            OutString += LocalKey.Key[7]
        if (Text[Counter] == 'I' or Text[Counter] == 'i'):
            OutString += LocalKey.Key[8]
        if (Text[Counter] == 'J' or Text[Counter] == 'j'):
            OutString += LocalKey.Key[9]
        if (Text[Counter] == 'K' or Text[Counter] == 'k'):
            OutString += LocalKey.Key[10]
        if (Text[Counter] == 'L' or Text[Counter] == 'l'):
            OutString += LocalKey.Key[11]
        if (Text[Counter] == 'M' or Text[Counter] == 'm'):
            OutString += LocalKey.Key[12]
        if (Text[Counter] == 'N' or Text[Counter] == 'n'):
            OutString += LocalKey.Key[13]
        if (Text[Counter] == 'O' or Text[Counter] == 'o'):
            OutString += LocalKey.Key[14]
        if (Text[Counter] == 'P' or Text[Counter] == 'p'):
            OutString += LocalKey.Key[15]
        if (Text[Counter] == 'Q' or Text[Counter] == 'q'):
            OutString += LocalKey.Key[16]
        if (Text[Counter] == 'R' or Text[Counter] == 'r'):
            OutString += LocalKey.Key[17]
        if (Text[Counter] == 'S' or Text[Counter] == 's'):
            OutString += LocalKey.Key[18]
        if (Text[Counter] == 'T' or Text[Counter] == 't'):
            OutString += LocalKey.Key[19]
        if (Text[Counter] == 'U' or Text[Counter] == 'u'):
            OutString += LocalKey.Key[20]
        if (Text[Counter] == 'V' or Text[Counter] == 'v'):
            OutString += LocalKey.Key[21]
        if (Text[Counter] == 'W' or Text[Counter] == 'w'):
            OutString += LocalKey.Key[22]
        if (Text[Counter] == 'X' or Text[Counter] == 'x'):
            OutString += LocalKey.Key[23]
        if (Text[Counter] == 'Y' or Text[Counter] == 'y'):
            OutString += LocalKey.Key[24]
        if (Text[Counter] == 'Z' or Text[Counter] == 'z'):
            OutString += LocalKey.Key[25]
        if (Text[Counter] == ' '):
            OutString += ' '            
        if (Text[Counter] == '0'):
            OutString += '9'
        if (Text[Counter] == '1'):
            OutString += '8'
        if (Text[Counter] == '2'):
            OutString += '7'
        if (Text[Counter] == '3'):
            OutString += '6'
        if (Text[Counter] == '4'):
            OutString += '5'
        if (Text[Counter] == '5'):
            OutString += '4'
        if (Text[Counter] == '6'):
            OutString += '3'
        if (Text[Counter] == '7'):
            OutString += '2'
        if (Text[Counter] == '8'):
            OutString += '1'
        if (Text[Counter] == '9'):
            OutString += '0'
            

def AddOrder(Name, Address, Number, ID):
    OrderFile = open("Order.list", "w+")
    OrderFile.write(str("Order: Name - " + Encrypt(Name) + " - Number - " + Encrypt(Number)  + " - Address - " + Encrypt(Address) + "\n"))
    OrderFile.close

def Fix(Text):
    return Text[0:len(Text)-1]

s = socket.socket()  
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    InData = str(conn.recv(1024))
    ParsedCommand = InData[2:len(InData) - 1]
    
    print(ParsedCommand)

    if (ParsedCommand.split(":")[0] == "BAL"):
        data = bytes(ServerBalanceInfo[Fix(InData.split(":")[1])], 'utf-8')
        conn.send(data)
        conn.close()
        s.listen()

    if (ParsedCommand.split(":")[0] == "ADD"):
        ServerBalanceInfo.update({Fix(InData.split(":")[1]):"0"})
        print(ServerBalanceInfo.items())
        conn.close()
        s.listen()

    if (ParsedCommand.split(":")[0] == "ORD"):

        Name = InData.split(":")[1]
        Number = InData.split(":")[3]
        Address = InData.split(":")[2]
        

        OrderFile = open("Order.list", "w+")
        OrderFile.write(str("Order: Name - " + Name + " - Number - " + Number  + " - Address - " + Address + "\n"))
        OrderFile.close

        OrderCost = int(str(InData.split(":")[4]))

        Balance = int(ServerBalanceInfo[InData.split(":")[1]])
        print(str(str("S: " + OrderCost - Balance)))
    
        conn.close()
        s.listen()
