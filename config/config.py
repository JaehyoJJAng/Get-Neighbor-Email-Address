from typing import Dict
import os
import json

BASE_DIR : str = '.login_info/.login.json'
def get_login_secrets(key:str)-> None:
    with open(BASE_DIR,'r',encoding='UTF-8') as fp:
        secrets : Dict[str,str] = json.loads(fp.read())    
    try:
        return secrets[key]
    except EnvironmentError:
        raise EnvironmentError(f'Set The {key}')