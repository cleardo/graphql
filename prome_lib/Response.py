# -*- coding:utf-8 -*-
from config import prome_config as con
from config.set_dev import *
import requests
import json


def get_response(env):
    # 获取sandbox环境token
    if env == "sandbox":
        sandbox = GetConfig()
        sandbox.settingconfig(env=env, proxies=con.base_proxies, debug=con.base_debug)
        payload = json.dumps(sandbox.account)
        r = requests.post(sandbox.login_host, data=payload, headers=sandbox.header)
        return r.text
    # 获取dev环境token
    elif env == "dev":
        dev = GetConfig()
        dev.settingconfig(env=env, proxies=con.base_proxies, debug=con.base_debug)
        payload = json.dumps(dev.account)
        r = requests.post(dev.login_host, data=payload, headers=dev.header)
        return r.text


def get_token(env):
    res = get_response(env=env)
    res = json.loads(res)
    token_value = res['AuthenticationResult']['IdToken']
    token_value = "{\"Authorization\": \"Bearer " + token_value + "\"}"
    return token_value


def show_token():
    token_value = get_token(con.show_token)
    print token_value


if __name__ == '__main__':
    show_token()
