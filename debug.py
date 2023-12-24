#from dependancies.sql.module import StartDBInstance, DBFunction
#Instance = StartDBInstance(creds={'user':'root','password':'pufpoLM10$!','host':'localhost','db':'lillith'})
#print(DBFunction(functionName='rawblob', arguments=['1'], instance=Instance))


creds={'user':'alex','password':'pufpoLM10$!','host':'10.0.0.70','db':'lillith'}

## Import modules safely into the current Lillith instance. Other wise throw an error and exit.

try:
    from colorama import Fore, Back, Style
    import sys, uvicorn, os
    from libraries.error_handler.module import *
    from fastapi import FastAPI, HTTPException, Depends, UploadFile
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
    from fastapi.responses import HTMLResponse
    from typing import Union
except ImportError as importException:
    #raise Exception(Fore.RED+'Import Error: ' + str(importException)+Style.RESET_ALL)
    sys.exit(Fore.RED+'Import Error: ' + str(importException)+Style.RESET_ALL)

try:
    from libraries.auth.web.module import *
    from libraries.data.module import *
    from dependancies.sql.workaround.blob import *

except ImportError as importException:
    raise Exception(f'Import Error: {str(importException.name)} - ignoring module but this may cause issues.')

os.system('cls' if os.name == 'nt' else 'clear')

## Define the API routes for Lillith.
print(BlobHandler(creds=creds, Mime='1234',blob='this is a test'))