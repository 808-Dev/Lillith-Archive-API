##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith. 
##------------------------------------------------------------------ 

creds= {'user':'',
        'password':'',
        'host':'',
        'db':'lillith'}

## Import modules safely into the current Lillith instance. Otherwise throw an error and exit.

try:
    from colorama import Fore, Back, Style
    import sys, uvicorn, os, base64
    from libraries.error_handler.module import *
    from fastapi import FastAPI, HTTPException, Depends, UploadFile
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
    from fastapi.responses import HTMLResponse, FileResponse
    from typing import Union
except ImportError as importException:
    ##raise Exception('Import Error: ' + str(importException)) ##Used for debugging only.
    sys.exit('Import Error: ' + str(importException))

try:
    from libraries.auth.web.module import *
    from libraries.data.module import *
except ImportError as importException:
    print(f'Import Error: {str(importException.name)} - ignoring module but this may cause issues.')
print('Importing quickpatches')
try:
    from dependancies.sql.workaround.blob import *
except:
    print(f'Import Error: {str(importException.name)} - ignoring module but usually this breaks critical functions.')

authorizedUrls = ("https://localhost:8000/","https://127.0.0.1:8000/")

app = FastAPI(title="Lillith API", description="This is the official API for Lillith.", version="1.00",
              terms_of_service='https://saliibot.com/about/eula/', summary="This is the official API for Lillith.io", docs_url=None, redoc_url=None)
              #servers=[{"url": authorizedUrls}])
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="authorize")

os.system('cls' if os.name == 'nt' else 'clear')

## Define the API routes for Lillith.

@app.get("/",tags=["API"], summary="This is the root endpoint for Lillith.")
async def groot(): 
    return hardCode()

##------------------------------------------------------------------
##Authorize API Access
##------------------------------------------------------------------

@app.post("/api", tags=["Authorization"], summary="This is the authorization endpoint for Lillith for 3rd party usage.")
def papitoken(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        return(webAuth(str(form_data.username), str(form_data.password), creds))
    except Exception as exception:
        raise HTTPException(status_code=403, detail=f'Unable to authenticate user: {str(form_data.username)}')

@app.post("/authorize", tags=["Authorization"], summary="This is the authorization endpoint for Lillith for in system usage (Writing operations limited).")
def ptoken(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        return(webAuth(str(form_data.username), str(form_data.password), creds))
    except Exception as exception:
        raise HTTPException(status_code=403, detail=f'Unable to authenticate user: {str(form_data.username)}')

##------------------------------------------------------------------
##Get Raw Blob Data  //TODO: Fix temp code for blobs
##------------------------------------------------------------------

@app.get("/blob/{blobID}", tags=["Data Handling"], summary="This is the endpoint for getting raw data.")
def gblob(blobID: str):
    try:
        blobData = getBlob(str(blobID), creds)
        mimeType= json.loads(json.loads(blobData[0])['meta_data'])['mime_type']
        #return(base64.b64decode(json.loads(blobData[0])['raw_data'][15:]))
        return(HTMLResponse(content=base64.b64decode(json.loads(blobData[0])['raw_data'][15:]),media_type=mimeType))
    except Exception as exception:
        raise HTTPException(status_code=500, detail=f'Unable to retrieve blob: {str(blobID)}')


##------------------------------------------------------------------
##Create new data
##------------------------------------------------------------------

@app.post("/post/{pid}/", tags=["Instances Handling"], summary="This is the endpoint for creating new data.")

def ppost(blobarray: Union[str,None] = None, pid: Union[int, None] = None, data: Union[str, None] = None, token: str = Depends(oauth2_schema)):
    #try:
        return(instanceHandler(pid, data, blobarray, creds))
    #except Exception as exception:
    #    raise HTTPException(status_code=500, detail=f'Unable to post instance: {str(data)}, error data: {exception}')

##------------------------------------------------------------------
##Create new datablob
##------------------------------------------------------------------

@app.post("/blob/", tags=["Datablob Handling","Data"], summary="This is the endpoint for creating new blobs.")

async def pblob(blobdata: UploadFile):
    datastream = await blobdata.read()
    mimedata = blobdata.content_type
    return(blobHandler(datastream, mimedata, creds))

##------------------------------------------------------------------
##Search for relational data
##------------------------------------------------------------------

@app.get("/relation/id/{id}", tags=["Relation Handling","Search"], summary="This is the endpoint for getting related data.") 

async def grelid(id: int):

    return(getRelationId(id, creds))

@app.get("/relation/tag/{tag}", tags=["Relation Handling","Search"], summary="This is the endpoint for getting related data.") 

async def greltag(tag: str):
    return(getRelationTag(tag, creds))

##------------------------------------------------------------------
##Search for instances
##------------------------------------------------------------------

@app.get("/instance/id/{id}", tags=["Instance Handling","Search"], summary="This is the endpoint for getting raw data.")

async def gid(id: int):
    return(getRawInstance(id, creds))

##------------------------------------------------------------------
##Create new instance
##------------------------------------------------------------------

@app.post("/instance", tags=["Data", "Instance Handling"], summary="This endpoint creates an instance.")

async def pinstance():
    return(newInstance(creds))


##------------------------------------------------------------------
## Get instance.
##------------------------------------------------------------------

@app.get("/instance/{id}", tags=["Data", "Instance Handling"], summary="This endpoint returns an instance.")

async def ginstance(id):
    return(getInstance(id, creds))

##------------------------------------------------------------------
## Get instances.
##------------------------------------------------------------------

@app.get("/instance/tag/{tag}", tags=["Data", "Instance Handling","Search"], summary="This endpoint returns a list instances that have that tag.")

async def ginstancetag(tag: Union[str, None] = ''):
	try:   
		return(getInstanceTag(str(tag), creds))
	except Exception as exception:
		raise HTTPException(status_code=200, detail=['empty'])


##------------------------------------------------------------------
## Get instances list.
##------------------------------------------------------------------

async def ginstancetag(tag: Union[str, None] = ''):
	try:   
		return(getInstanceTag(str(tag), creds))
	except Exception as exception:
		raise HTTPException(status_code=200, detail=['empty'])

##------------------------------------------------------------------
## Get latest datablob list.
##------------------------------------------------------------------

@app.get("/instance/latest/", tags=["Data","Instance Handling","Search"], summary="This endpoint returns a list of the latest relations.")

async def ginstancelatest():
	return(getLatestInstances(creds))

##------------------------------------------------------------------
## Get datablob array.
##------------------------------------------------------------------

@app.get("/blob/meta/{id}", tags=["Blobs","Datablob Handling","Meta Data"], summary="This endpoint returns an array of variables associated with the data being looked up.")

async def gblobdata(id: Union[str, None] = ''):
	return(getblobdata(creds, str(id)))



@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html_cdn():
    return get_swagger_ui_html(
    openapi_url=app.openapi_url,
    title=f"{app.title} - Swagger UI",
    # swagger_ui_dark.css CDN link
    swagger_css_url='/css'
)

@app.get("/css", include_in_schema=False)
async def custom_swagger_ui_html_cdn():
	return(FileResponse('./css/custom.css'))

##------------------------------------------------------------------
## Run the instance of Lillith.
##------------------------------------------------------------------

if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
