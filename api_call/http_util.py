# coding=utf-8

from nd.rest.co_token.uc import *

__author__ = 'Administrator'


class HttpUnity(object):
    def __init__(self, env):
        self.env = env

        # 声明默认的http对象（声明后才有具体实例）、header（设置后才生效）、版本号等
        self.http_o = None
        self.host = None
        self.port = None
        self.token_o = None

        self.header = dict()
        self.header['Accept'] = 'application/json'
        self.header['Content-Type'] = 'application/json'

        self.version = '1'

    def get_url(self, url):
        """
        url前面的'/'应该是包含在url里的，所以在版本号和url之间不加'/'
        """
        return "/v" + str(self.version) + url

    def set_token(self):
        """
        根据环境，指定uc不同环境的token实例
        """
        if self.env == 'ol':
            uc_env = UcEnv.ol
        else:
            uc_env = UcEnv.pre
        self.token_o = UcToken(uc_env)

    def set_http(self):
        """
        获取http实例
        """
        self.http_o = Http(self.host, self.port)
        self.http_o.set_header(self.header)

    def remove_authorization(self):
        if 'Authorization' in self.header.keys():
            self.header.pop('Authorization')
            self.http_o.set_header(self.header)

    def remove_cookie(self):
        if 'Cookie' in self.header.keys():
            self.header.pop('Cookie')
            self.http_o.set_header(self.header)

    def get(self, url):
        url = self.get_url(url)
        res = self.http_o.get(url)
        return res

    def post(self, url, param=None):
        url = self.get_url(url)
        param = json.dumps(param)
        res = self.http_o.post(url, param)
        return res

    def put(self, url, params=''):
        url = self.get_url(url)
        param = json.dumps(params)
        res = self.http_o.put(url, param)
        return res

    def delete(self, url, param=""):
        url = self.get_url(url)
        if param == "":
            res = self.http_o.delete(url)
        else:
            params = json.dumps(param)
            res = self.http_o.delete(url, params)
        return res
