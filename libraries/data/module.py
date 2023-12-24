##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith.
##------------------------------------------------------------------ 
import sys
from dependancies.sql.module import *
def getBlob(id=None, instance={}):
    Instance = StartDBInstance(instance)
    if id:
        rawData = DBFunction(functionName='rawblob', arguments=[id], instance=Instance)
        return(rawData)
    else:
        return returnException(3)
    
def postInit(data, token, creds):
    Instance = StartDBInstance(creds)
    if data != None and token != None:
        return(data)

def hardCode():
    return({
            "apihost":["https://api.lillith.io","https://tcode.808-dev.com","https://api.saliibot.com"],
            "authhost":["https://api.lillith.io/auth","https://tcode.808-dev.com/auth","https://api.saliibot.com/auth"],
            "type":"monolithic","documentation":["https://api.lillith.io/docs","https://api.saliibot.com/docs","https://tcode.808-dev.com/docs"]
            })

#def blobHandler(data, mimedata, creds):
#    Instance = StartDBInstance(creds)
#    return DBBlobSetup(functionName='set_blob',arguments=[data,mimedata],instance=Instance)
#Check dependancies/sql/workarounds/blob.py for this function. This isn't working for some reason when using blobs.

def getRelationId(id, creds):
    Instance = StartDBInstance(creds)
    return json.loads(DBFunction(functionName='relationbyid', arguments=[id], instance=Instance)[0])

def getRelationTag(tag, creds):
    Instance = StartDBInstance(creds)
    return json.loads(DBFunction(functionName='relationbytag', arguments=[tag], instance=Instance)[0])

def getRawInstance(id, creds):
    Instance = StartDBInstance(creds)
    return DBFunction(functionName='rawinstance', arguments=[id], instance=Instance)

def instanceHandler(data, blobarray, creds):
    Instance = StartDBInstance(creds)
    
    template = {
        "Raw_Data": data['raw'],
        "Instance": {
            "Properties": {
                "Title": data['properties']['title'],
                "Summary": data['properties']['summary'],
                "URL": data['properties']['url'],
                "favicon": data['properties']['favicon'],
                "id": data['properties']['id'],
                "platform": data['properties']['platform']
            },
            "Media": [0],  # Assuming this is a placeholder, adjust as needed
            "Data": data['variables']
        }
    }

    try:
        result = DBFunction(functionName='set_instance', arguments=[23,json.dumps(template)], instance=Instance)
    except Exception as e:
        print(f"Error: {e}")


    return result

def newInstance(creds):
    Instance = StartDBInstance(creds)
    try:
        return(DBFunction(functionName='initinstance', arguments=[], instance=Instance)[0])
    except Exception as e:
        print(f"Error: {e}")

def initblob(blob, mimetype, creds):
    Instance = StartDBInstance(creds)

    try:
        return(DBFunction(functionName='set_blob', arguments=[122, blob, mimetype], instance=Instance)[0])
    except Exception as e:
        print(f"Error: {e}")

def getInstance(id, creds):
    Instance = StartDBInstance(creds)
    return json.loads(DBFunction(functionName='getinstance', arguments=[id], instance=Instance)[0])