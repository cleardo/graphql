# coding=utf-8

from api_call.http_util import *
from nd.rest.conf.conf import MyCfg


__author__ = 'Administrator'


class BaseHttp(HttpUnity):
    def __init__(self, env=None, language=None):
        """
        :param env: 指定配置文件中的环境名称
        """
        super(BaseHttp, self).__init__(env)
        self.env = env
        self.language = language

        # 1.读配置文件，获取host等配置
        my_cfg = MyCfg('channel_gateway.ini')
        my_cfg.set_path(__file__)
        my_cfg.set_section(self.env)

        self.host = my_cfg.get("host")
        try:
            self.port = my_cfg.get("port")
        except Exception as e:
            print e

        self.gaea_id = my_cfg.get("gaea_id")
        self.user = my_cfg.get("user")
        self.password = my_cfg.get("password")

        # 声明http、token实例
        self.set_http()
        self.set_token()

        # self.header['Accept-Language'] = 'zh-CN,zh;q=0.8'   # 中文
        # self.header['Accept-Language'] = 'th'             # 泰文
        # self.header['Accept-Language'] = 'en-us'          # 英文

    def set_auth(self, token_type=2, user_name='', password='', org='', url='', method=''):
        """
        设置身份信息
        无指定的身份信息时，直接使用默认的身份
        token_type:
            0: header中，不使用Authorization
            1：token 错误
            其他：header中带Authorization
        user_name、password： 切换登录者时传入，不传，默认使用设置的账号
        """
        if user_name == '':
            user_name = self.user
        if password == '':
            password = self.password

        host = self.host
        if self.port != '' and self.port is not None:
            host += ':' + str(self.port)

        # 使用 gaea_id 隔离项目数据
        self.header['X-Gaea-Authorization'] = 'GAEA id="' + str(self.gaea_id) + '"'

        if token_type == 0:
            self.remove_authorization()
        elif token_type == 1:     # 设置为错误的mac token
            self.header['Authorization'] = \
                'MAC id="930F04593E040BDAE507E54C00B84C4059008269612143E0835D2B9ED7C01C23",' \
                'nonce="1470724550000:9Sl9pGRo",mac="PRcoAuUzDZsrIxrcX+Pm+AYp+YI5ttR+KsRbdGJn8Ys="'
        else:
            access_token = self.token_o.get_token(user_name, password, org, self.get_url(url), method, host)
            self.header['Authorization'] = access_token
            self.http_o.set_header(self.header)
