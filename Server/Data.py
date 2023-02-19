
def Fix(Text):
    return Text[0:len(Text)-1]

def PullAddress():
    ConfFile = open("Address.conf", "r+")
    Address = ConfFile.read()
    ConfFile.close
    return Address


Host = PullAddress()
Port = 12345

OrderCounter = 0

ServerBalanceInfo = { 
    # Balance Dictionary
}

def CheckItem(Dictionary, Item):
    try:
        print(Dictionary[Item])
        return True
    except:
        return False