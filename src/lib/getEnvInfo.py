# coding=utf-8
from src.setting.setting import *
import logging


def getEnvInfo():
    envInfo = {}

    if USE_ENV == "dev":
        envInfo['host'] = "https://devapi.prometheanproduct.com"
        envInfo['loginApi'] = "https://devapi.prometheanproduct.com/identity/login"
        envInfo['account'] = {
            "email": "yy949177@nd.com.cn",
            "password": "NetDragon91"
        }
        envInfo['header'] = {
            'x-api-key': "b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg",
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        return envInfo

    if USE_ENV == "sandbox":
        envInfo['host'] = "https://sandboxapi.prometheanproduct.com"
        envInfo['loginApi'] = "https://sandboxapi.prometheanproduct.com/identity/login"
        envInfo['account'] = {
            "email": "yy949177@nd.com.cn",
            "password": "NetDragon91"
        }
        envInfo['header'] = {
            'x-api-key': "l4mfs8uak1wglsxsyr4ada8h0d0179fwwlrgrzxg",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        return envInfo

    if USE_ENV == "stage":
        envInfo['host'] = "https://stagingapi.mypromethean.com"
        envInfo['loginApi'] = "https://stagingapi.mypromethean.com/identity/login"
        envInfo['account'] = {
            "email": "xiaoyong.zhou@gmail.com",
            "password": "ClassFlow2018"
        }
        envInfo['header'] = {
            'x-api-key': "m3r8nquap6mn44l93vyu0cf08qd9vd8169l68zfn",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        return envInfo

    else:
        logging.error('[环境配置错误] - [未配置环境{envInfo}, 请在src.lib.ENV.py添加配置]'.format(envInfo=envInfo))
