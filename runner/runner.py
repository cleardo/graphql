#!/usr/bin/python
# -*- coding: utf-8 -*

import sys
sys.path.insert(0, '/home/linzh/workspace/prome/graphql')
import requests
import HTMLTestRunner
import time
import json
from testcases.testsuite import suite
from config import prome_config as con

if __name__ == '__main__':
    if con.HTMLreportPath and len(con.HTMLreportPath) != 0:
            HTMLfilepath = con.HTMLreportPath
    else:
        HTMLfilepath = "./report"
    if con.mdm_portal_env == "dev":
        prefix = "PM-Test-Dev"
    elif con.mdm_portal_env == "sandbox":

	prefix = "PM-Test-Sadnbox"
    TimeStr = prefix + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.html'

    filename = HTMLfilepath+TimeStr
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'PM Panel Management API Test',
                                           description=u'PM Panel Management API Test')
    runner.run(suite)

    hooks_url = "https://hooks.slack.com/services/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"
    header = {
        'content-type': "application/json"
    }
    payload = """{"text":"<!here>Panel Management接口测试报告%s：http://54.183.7.44/%s"}""" % (TimeStr, TimeStr)
    print payload
    # response = requests.post(hooks_url, headers=header, data=payload)
    # r = json.dumps(response.text)
    # print '\n*** response ***: \n', json.dumps(r, indent=4, sort_keys=True), '\n'