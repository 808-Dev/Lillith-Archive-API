##SVN 1.01
##Author: Alex Merriam
##Date: 10-26-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith.
##------------------------------------------------------------------ 
from dependancies.sql.module import *
def getBlob(id=None, instance={}):
    Instance = StartDBInstance(instance)
    if id:
        rawData = DBFunction(functionName='rawblob', arguments=[str(id)], instance=Instance)

        return(rawData)
    else:
        return returnException(3)
    
def postInit(data, token, creds):
    Instance = StartDBInstance(creds)
    if data != None and token != None:
        return(data)

def hardCode():
    return({
            "apihost":["https://api.lillith.io","https://localhost:8000","https://api.saliibot.com"],
            "authhost":["https://api.lillith.io/auth","https://localhost:8000/auth","https://api.saliibot.com/auth"],
            "type":"monolithic",
            })