import os
putenv = lambda key,value:os.environ(key,value)
try:
    token=os.environ.get('API_token_bot')
    P,Z,N=os.environ.get("PZN",'').split('\\')
except:
    ston=__import__('ston')
    token=ston.token
    P,Z,N=ston.P,ston.Z,ston.N
