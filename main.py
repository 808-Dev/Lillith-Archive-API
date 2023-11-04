##SVN 1.01
##Author: Alex Merriam
##Date: 10-26-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith.
##------------------------------------------------------------------ 

creds={'user':'root','password':'pufpoLM10$!','host':'localhost','db':'lillith'}

## Import modules safely into the current Lillith instance. Other wise throw an error and exit.

try:
    import sys, uvicorn, os
    from libraries.error_handler.module import *
    from fastapi import FastAPI, HTTPException, Depends, UploadFile
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
    from fastapi.responses import HTMLResponse
    from typing import Union
except ImportError as importException:
    raise Exception('Import Error: ' + str(importException))
    sys.exit('Import Error: ' + str(importException))

try:
    from libraries.auth.web.module import *
    from libraries.data.module import *
except ImportError as importException:
    raise Exception(f'Import Error: {str(importException.name)} - ignoring module but this may cause issues.')

authorizedUrls = ("https://localhost:8000/","https://127.0.0.1:8000/")

app = FastAPI(title="Lillith API", description="This is the official API for Lillith.", version="23.10",
              terms_of_service='https://saliibot.com/about/eula/', summary="This is the official API for Lillith",)
              #servers=[{"url": authorizedUrls}])
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="authorize")

os.system('cls' if os.name == 'nt' else 'clear')


## Define the API routes for Lillith.

@app.get("/",tags=["API"], summary="This is the root endpoint for Lillith.")
async def root():
    return hardCode()
##------------------------------------------------------------------
##Authorize API Access
##------------------------------------------------------------------

@app.post("/api", tags=["Authorization"], summary="This is the authorization endpoint for Lillith for 3rd party usage.")
def apitoken(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        return(webAuth(str(form_data.username), str(form_data.password), creds))
    except Exception as exception:
        raise HTTPException(status_code=403, detail=f'Unable to authenticate user: {str(form_data.username)}')

@app.post("/authorize", tags=["Authorization"], summary="This is the authorization endpoint for Lillith for in system usage (Writing operations limited).")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        return(webAuth(str(form_data.username), str(form_data.password), creds))
    except Exception as exception:
        raise HTTPException(status_code=403, detail=f'Unable to authenticate user: {str(form_data.username)}')

##------------------------------------------------------------------
##Get Raw Blob Data  //TODO: Fix what ever is wrong with this.
##------------------------------------------------------------------

#@app.get("/blob/{blobID}", tags=["Data Handling"], summary="This is the endpoint for getting raw data.")
#def gblob(blobID: str):
    #try:
    #    return(HTMLResponse(content=getBlob(str(blobID), creds),media_type="image/jpeg"))
    #except Exception as exception:
    #    raise HTTPException(status_code=500, detail=f'Unable to retrieve blob: {str(blobID)}')


##------------------------------------------------------------------
##Create new data
##------------------------------------------------------------------

@app.post("/post/", tags=["Data Handling"], summary="This is the endpoint for creating new data.")

def post(data: Union[str, None] = None, token: str = Depends(oauth2_schema)):
    try:
        return(postBlob(data, token, creds))
    except Exception as exception:
        raise HTTPException(status_code=500, detail=f'Unable to post blob: {str(data)}')



## Run the instance of Lillith.
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

