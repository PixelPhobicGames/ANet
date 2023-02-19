

def CenterText(Text , Width):
    Length = len(Text)
    return (Width / 2) - ((Length * 7) / 2)

def ScaleValue(Original , Width):
    ScaleFactor = Width / 600
    return Original * ScaleFactor

