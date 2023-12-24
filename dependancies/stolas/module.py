##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial Stolas hash verifier.
##------------------------------------------------------------------ 

def stolas(data = None):
    StolasSaltCompiled = ""
    HexArray = ['A','B','C','D','E','F']
    hexSum = 0
    for HexCharacter in HexArray:
        if(HexCharacter in data.upper()):    
            dataconvert = data.upper()
            StolasSaltCompiled = StolasSaltCompiled + HexCharacter + str(dataconvert.count(HexCharacter))
            hexSum = hexSum + int(dataconvert.count(HexCharacter))
    return(f"{StolasSaltCompiled}Z{hexSum}")