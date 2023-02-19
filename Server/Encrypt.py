


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
            
        Counter += 1
        
    return OutString