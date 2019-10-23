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
    try:HTMLfilepath = con.HTMLreportPath
    except: HTMLfilepath = "./report"
    finally: None
    if con.mdm_portal_env == "dev":
        prefix = "PM-Test-Dev"
    elif con.mdm_portal_env == "sandbox":
        prefix = "PM-Test-Sadnbox"
    elif con.mdm_portal_env == "stage":
        prefix = "PM-Test-Stage"
    TimeStr = prefix + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.html'

    filename = HTMLfilepath+TimeStr
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'PM Panel Management API Test',
                                           description=u'PM Panel Management API Test')
    runner.run(suite)
    if sys.argv[1] == "sendreport":
        hooks_url = "https://hooks.slack.com/services/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"
        header = {
            'content-type': "application/json"
        }
        payload = """{"text":"Panel Management接口测试报告%s：http://54.183.7.44/%s"}""" % (TimeStr, TimeStr)
        print payload
        response = requests.post(hooks_url, headers=header, data=payload)
        r = json.dumps(response.text)
        print '\n*** response ***: \njson.dumps(r, indent=4, sort_keys=True)'
    else:
        pass