def GenerateIDInfo(Name , Phone , Pass):
    ConfFile = open("AppData/User/User.conf", "w")
    ConfFile.write(Name + "\n")
    ConfFile.close

    print()

def PullID():
    return 0