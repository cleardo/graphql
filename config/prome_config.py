# -*- coding:utf-8 -*-

# 基础环境设置
# 设置Socket5 代理
base_debug = True
# Socket5代理地址
base_proxies = {
        'http': 'http://127.0.0.1:1080',
        'https': 'http://127.0.0.1:1080'
}

# get_token = dev, sandbox
show_token = "dev"

# env = dev, sandbox
mdm_portal_env = "dev"
configuration_env = "dev"


# 设置 HTML 报告存放路径
HTMLreportPath = "/var/www/report/"

# 设置测试模式, Ture为自动，False为指定参数模式
# 具体使用参考docs中使用手册
AutoTestMode = True

