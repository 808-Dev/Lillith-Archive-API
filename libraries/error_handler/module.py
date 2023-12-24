##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith.
##------------------------------------------------------------------ 
def returnException(errorCode, errorMsg=None):
    if errorCode:
        if errorCode == 1:
            return('A general error has occurred within the API.')
        if errorCode == 2:
            return('A dependancy error has occurred within the API.')
        if errorCode == 3:
            return('A malformed request was sent to the API.')
        if errorCode == 4:
            return('An improper request was sent to the API.')
        if errorCode == 5:
            return('A critical error has occurred. Ending instance for system stability.')
        if errorCode == 6:
            return('Debug: '+errorMsg)
def exceptionList():
    return([1,2,3,4,5,6])