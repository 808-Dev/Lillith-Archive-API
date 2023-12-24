##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith.
##------------------------------------------------------------------ 
from dependancies.sql.module import *
import json
def webAuth(username=None, password=None, instance={}):
    Instance = StartDBInstance(instance)
    if username and password:
            return{"access_token":json.loads(str(DBFunction(functionName='lillithlogin', arguments=[username,password,'FAS'], instance=Instance)[0])),
                   "token_type": "bearer"}
    else:
        return returnException(3)