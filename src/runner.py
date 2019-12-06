# coding=utf-8
import sys
import os
sys.path.insert(0, os.getcwd()[:-3])

from src.lib import HTMLTestRunner
from src.lib.operateData import *
from src.setting.setting import *
import unittest


def runner():
    # 实例化测试套件对象
    suite = unittest.TestSuite()
    # 实例化TestLoader的对象
    loader = unittest.TestLoader()
    # 寻找当前目录下的所有测试文件
    suite.addTests(loader.discover(os.getcwd()))

    fileName = USE_ENV + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.html'
    fp = open(HTML_REPORT_PATH + fileName, 'wb')

    # 生成HTML报告
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'PM Panel Management API Test',
                                           description=u'PM Panel Management API Test')
    runner.run(suite)
    fp.close()

    # 发送提示
    if sys.argv[1] == "sendreport":
        hooks_url = "https://hooks.slack.com/services/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"
        header = {'content-type': "application/json"}
        payload = '{"text":"Panel Management接口测试报告：http://54.183.7.44/report/%s"}' % fileName
        requests.post(hooks_url, headers=header, data=payload)
    else:
        pass

# if __name__ == '__main__':
#     import sys
#     import os
#     sys.path.insert(0, os.getcwd()[:-3])
#     runner()
