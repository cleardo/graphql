# coding=utf-8
class GetConfig(object):
    def __init__(self):
        self.login_host = ""
        self.api_key = ""
        self.account = ""
        self.header = {}
        self.DEBUG = False
        self.proxies = {}
        self.host = ""

    def settingconfig(self, env, debug, proxies):
        if env == "dev":
            self.login_host = "https://devapi.prometheanproduct.com/identity/login"
            self.api_key = "b0p31d5rm8ifd93132cfolmsa01yc60u4nd79btg"  # dev api
            self.account = {
                "email": "yy949177@nd.com.cn",
                "password": "NetDragon91"
            }
            self.header = {
                'x-api-key': self.api_key,
                'content-type': "application/json",
                'cache-control': "no-cache",
            }
            self.DEBUG = debug
            self.proxies = proxies
            self.host = "https://devapi.prometheanproduct.com"
        elif env == "sandbox":
            self.login_host = "https://sandboxapi.prometheanproduct.com/identity/login"
            self.api_key = "l4mfs8uak1wglsxsyr4ada8h0d0179fwwlrgrzxg"
            self.account = {
                "email": "yy949177@nd.com.cn",
                "password": "NetDragon91"
            }
            self.header = {
                'x-api-key': self.api_key,
                'content-type': "application/json",
                'cache-control': "no-cache",
            }
            self.DEBUG = debug
            self.proxies = proxies
            self.host = "https://sandboxapi.prometheanproduct.com"
        elif env == "stage":
            self.login_host = "https://stagingapi.mypromethean.com/identity/login"
            self.api_key = "m3r8nquap6mn44l93vyu0cf08qd9vd8169l68zfn"
            self.account = {
                "email": "xiaoyong.zhou@prometheanworld.com",
                "password": "ClassFlow2018"
            }
            self.header = {
                'x-api-key': self.api_key,
                'content-type': "application/json",
                'cache-control': "no-cache",
            }
            self.DEBUG = debug
            self.proxies = proxies
            self.host = "https://stagingapi.mypromethean.com"
        return (self.login_host, self.account, self.api_key,
                self.account, self.header, self.DEBUG, self.proxies,
                self.host)
