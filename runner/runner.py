#!/usr/bin/python

# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/linzh/workspace/prome/graphql')
import HTMLTestRunner
import time
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
