##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith (This is a temporary fix to get around a commit issue with the blob uploader).
##------------------------------------------------------------------ 

from dependancies.sql.module import *
def blobHandler(blob=None,Mime=None, creds=None):
    AuthenticationNode = StartDBInstance(creds)

    Template = 'INSERT INTO datablobs (raw_data, meta_data, property_data, create_time) VALUES (%s, %s, %s, CURRENT_TIMESTAMP);'
    MimeSetup = json.dumps({"mime_type":Mime})
    DataSet = [blob, MimeSetup, json.dumps(())]
    try:
        return(SQLPostReversion(template=Template, data=DataSet, connection=AuthenticationNode))
    except:
        return(-1)

def SQLPostReversion(template,data,connection):
    SQLAutheticatedSession = connection[0]
    SQLSessionRaw = connection[1]
    SQLAutheticatedSession.execute(template, data)
    try:
        SQLSessionRaw.commit()
        return(SQLAutheticatedSession.lastrowid)
    except:
        return(False)
