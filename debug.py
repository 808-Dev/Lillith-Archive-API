from dependancies.sql.module import StartDBInstance, DBFunction
Instance = StartDBInstance(creds={'user':'root','password':'pufpoLM10$!','host':'localhost','db':'lillith'})
print(DBFunction(functionName='rawblob', arguments=['1'], instance=Instance))
