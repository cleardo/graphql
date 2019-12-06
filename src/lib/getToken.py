# -*- coding:utf-8 -*-
from src.lib.getEnvInfo import *
from src.setting.setting import *
import requests
import json


def getToken():
    env = getEnvInfo()
    payload = json.dumps(env['account'])
    r = requests.post(env['loginApi'], data=payload, headers=env['header'], proxies=(PROXY and PROXY_ADDRESS)).json()
    token = r['AuthenticationResult']['IdToken']
    return token


if __name__ == '__main__':
    token = getToken()
    print("{\"Authorization\": \"Bearer " + token + "\"}")
