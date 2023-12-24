##SVN 1.01
##Author: Alex Merriam
##Date: 12-24-2023
##------------------------------------------------------------------
##Notes: Initial API implementation for Lillith.
##------------------------------------------------------------------ 
import mysql.connector, mysql.connector.errors, json
from libraries.error_handler.module import *

def StartDBInstance(creds=(None,None,None,None)):
    if creds:
        try:
            Instance = mysql.connector.connect(host=creds['host'], user=creds['user'], password=creds['password'], database=creds['db'])
            return(Instance.cursor(),Instance)
        except mysql.connector.errors.ProgrammingError as exception:
            if exception.errno == 1045:
                return(returnException(6,'Invalid Credentials'))
            elif exception.errno == 1049:
                return(returnException(6,'Invalid Database'))
            else:
                return(returnException(6,exception))
    else:
        return(3) #Malformed request


def DBFunction(functionName=None, arguments=[None], instance=None):
    DB = instance[0]
    template = 'SELECT {}({});'.format(functionName, ', '.join(['%s']*len(arguments)))
    try:
        DB.execute(template, arguments)
        return(DB.fetchall()[0])
        instance[1].commit()
    except mysql.connector.Error as err:
        return(returnException(6,f'Exception occured while processing entity.\n\n Exception reason:\n\n{err.errno}'))

def TEMPDBBlobHandler(functionName=None, arguments=[None], instance=None):
    DB = instance[0]
    template = 'SELECT {}({});'.format(functionName, ', '.join(['%s']*len(arguments)))
    try:
        DB.execute(template, arguments)
        return DB.fetchall()[0]
    except mysql.connector.Error as err:
        return(returnException(6,f'Exception occured while processing entity.\n\n Exception reason:\n\n{err.errno}'))


def DBBlobSetup(functionName=None, arguments=[None], instance=None):
    DB = instance[0]
    template = 'SELECT {}({});'.format(functionName, ', '.join(['%s']*len(arguments)))
    try:
        DB.execute(template, arguments)
        instance[1].commit()  # Commit changes before fetching results
        return DB.fetchall()[0]
    except mysql.connector.Error as err:
        return returnException(6, f'Exception occurred while processing entity.\n\n Exception reason:\n\n{err.errno}')
