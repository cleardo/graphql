# coding=utf-8

"""pyquery-ql.py

Send a graphql query to GitHub
and pretty print output.

Usage:

    python3 pyquery-ql.py

Supports Python 3.6+

"""
import json
import logging
import pprint
import requests
from config import prome_config
from prome_lib import Response
from config.set_dev import *


class GraphqlQuery(object):

    # 接收Graphql语句，发送请求,     Get graphql query send query.

    def send_query(self, query, showprint=True, api='mdm-portal', url='', method='post'):

        # 获取 mdm_portal 参数
        if api == 'mdm-portal':
            env = GetConfig()
            env.settingconfig(env=prome_config.mdm_portal_env,
                              debug=prome_config.base_debug,
                              proxies=prome_config.base_proxies
                              )
            debug = env.DEBUG
            url = env.host+"/mdm-portal/graphql"
            logger = logging.getLogger(__name__)
            # 从get_token获取token键值对
            token = Response.get_token(prome_config.mdm_portal_env)
            token = json.loads(token)
            proxies = env.proxies
            headers = {}
            # add token to headers
            headers.update(token)
            # 发送 mdm_portal 请求
            method = "post"
            if debug is True:
                requests.packages.urllib3.disable_warnings()  # 屏蔽https 安全提示
                response = requests.request(method=method, url=url, json={'query': query},
                                            headers=headers, verify=False, proxies=proxies)
                # print 'proxy to %s now' % self.proxies
                # print self.proxies
            else:
                requests.packages.urllib3.disable_warnings()  # 屏蔽https 安全提示
                response = requests.request(method=method, url=url, json={'query': query},
                                            headers=headers, verify=False)

        # 发送 configuration 请求
        elif api == 'configuration':
            method = "post"
            env = GetConfig()
            env.settingconfig(env=prome_config.configuration_env,
                              debug=prome_config.base_debug,
                              proxies=prome_config.base_proxies
                              )
            debug = env.DEBUG
            url = env.host + '/configuration/graphql'
            logger = logging.getLogger(__name__)
            # 从get_token获取token键值对
            token = Response.get_token(prome_config.configuration_env)
            token = json.loads(token)
            proxies = env.proxies
            headers = {}
            # add token to headers
            headers.update(token)
            # 发送 mdm_portal 请求
            if debug is True:
                requests.packages.urllib3.disable_warnings()  # 屏蔽https 安全提示
                response = requests.request(method=method, url=url, json={'query': query},
                                            headers=headers, verify=False, proxies=proxies)
            else:
                requests.packages.urllib3.disable_warnings()  # 屏蔽https 安全提示
                response = requests.request(method=method, url=url, json={'query': query},
                                            headers=headers, verify=False)

        if showprint is True:
            # print token
            print '\n*** request ***: \n', query
            print "\n*** status code ***: ", response.status_code
            r = json.loads(response.text)
            print '\n*** response ***: \n', json.dumps(r, indent=4, sort_keys=True), '\n'
        if response.status_code == 200:
            return response
        else:
            # self.logger.warning(f"Request received error code: {result.status_code}")
            return response

# ----------------QUERIES Start ----------------
# 查询顺序按照Graphql-Web界面的Docs顺序

    # 通过页面号和偏移量获取 Panels 面板的信息,   Get Panel info by offset and pagesize.
    def panels(self, pageSize, offset, showprint=True):
        query = """
query Panels{
    Panels(searchPanelsInput:{pageSize:%d,offset:%d}){
        panels{
            name,
            serialNumber,
            model,
            mainboardFirmware,
            updateAvailable,
            otaVersion,
            tagCount,
            tags,
            connectivity,
            connectivityTimestamp,
            otaStatus,
            status
        }
        totalCount
    }
}
        """
        query = query % (pageSize, offset)
        response = self.send_query(query, showprint)
        body = json.loads(response.text)
        return response, body

    # 通过 SN 码获取面板的设备信息,     Get Panel device info by SN.
    def panel(self, serialNumber, showprint=True):
        query = """
query getPanelBySN{
    Panel(serialNumber:"%s"){
        summary{
        name
        serialNumber
        }
        bezelFirmware
        macAddress
        ipAddress
        tags{
            group
            groupId
            values{
                value
                id
            }
        }
    }
}
        """
        response = self.send_query(query % serialNumber, showprint)
        body = json.loads(response.text)
        return response, body

    # 获取标签信息,   Get tags info.
    def tags(self, showprint=True):

        query = """
query{
    Tags{
    group,
    values{
        id,value}
    }
}
        """
        response = self.send_query(query, showprint)
        body = json.loads(response.text)
        return response, body

    # 获取 ota 信息,    Get ota info.
    def ota(self):
        query = """
query{
    Ota{
        version
        notes
    }
}
        """
        response = self.send_query(query)
        body = json.loads(response.text)
        return response, body

    # 通过 SN 码获取 Panel 的指定页面的活动日志
    def activityLogs(self, serialNumber, pageSize, offset):
        page_query = ""
        offset_query = ""
        if pageSize:
            page_query = ", pageSize: " + str(pageSize)
        if offset:
            offset_query = ", offset: " + str(offset)
        query = """
query {
  ActivityLogs(searchActivityLog: {serialNumber:"%s" %s %s})
  {
    totalCount
    logs{
      createTime
      user
      panelName
      eventDetail
      event
      organization
      status
      serialNumber
    }
  }
}
        """
        query = query % (serialNumber, page_query, offset_query)
        response = self.send_query(query)
        body = json.loads(response.text)
        return response, body

    def modelList(self):
        query = """
query ModelList{
    ModelList
}
        """

        r = self.send_query(query)
        body = json.loads(r.text)
        return r, body

    def mainboardFirmwareList(self):
        query = """
query MainboardFirmwareList {
  MainboardFirmwareList
}
        """

        r = self.send_query(query)
        body = json.loads(r.text)
        return r, body

    def userList(self):
        query = """
query {
      UserList {
        user
        profileId
      }
    }
        """

        r = self.send_query(query)
        body = json.loads(r.text)
        return r, body

    def deployInfo(self):
        # 不用测，留个位置意思意思
        pass

    def enroll_validation(self, serialNumber, panelName=""):

        query = """
query{
    EnrollValidation(input: [{serialNumber: "%s", panelName: "%s"}])
    {
    isValid,
    error,
    }
}
                """
        query = query % (serialNumber, panelName)
        response = self.send_query(query)
        body = json.loads(response.text)
        return response, body

# ----------------QUERIES End ----------------

# ----------------MUTATIONS Start ----------------

    def updatePanelName(self, serialNumber, name):
            query = """
mutation{
    updatePanelName(updatePanelNameRequest:{serialNumber:"%s",name:"%s"}){
        name
        serialNumber
        model
        mainboardFirmware
        updateAvailable
        tagCount
        tags
    }
}
            """
            response = self.send_query(query % (serialNumber, name))
            body = json.loads(response.text)
            return response, body

    def createTag(self, group, tagname, showprint=True):
        create = """
mutation createTag {
    createTag(group: "%s", value:"%s") {
        id
        value
        group
    }
}
                """
        response = self.send_query(create % (group, tagname), showprint)
        body = json.loads(response.text)
        return response, body

    def deleteTag(self, tagid):
        query = """
mutation deleteTagById{
    deleteTag(id:"%s"){
        id,group,value
    }
}
        """
        response = self.send_query(query % tagid)
        body = json.loads(response.text)
        return response, body

    def updateTag(self, tagid, group, value):
        query = """
mutation {
    updateTag(id:"%s", group:"%s", value:"%s") {
        id,group,value
    }
}
            """
        response = self.send_query(query % (tagid, group, value))
        body = json.loads(response.text)
        return response, body

    def executeOta(self, SNList, delay=False, showprint=True):
        query = """
mutation {
   executeOta(serialNumberList:"%s")
}
               """
        response = self.send_query(query % SNList, showprint=showprint)
        body = json.loads(response.text)
        return response, body

    def addpanelTags(self, serialNumber, tagId, showprint=False):
        query = """
mutation{
 addPanelTags(addPanelTagsRequest:{serialNumber:"%s",tagId:"%s"})
}
                    """
        response = self.send_query(query % (serialNumber, tagId), showprint=showprint)
        body = json.loads(response.text)
        return response, body

    def updatepanelTags(self, serialNumber, tagId):
        query = """
mutation{
 updatePanelTags(updatePanelTagsRequest:{serialNumber:"%s",tagId:"%s"})
}
                   """
        response = self.send_query(query % (serialNumber, tagId))
        body = json.loads(response.text)
        return response, body

    def deletePanelTags(self, serialNumber, tagId):
        query = """
mutation{
 deletePanelTags(deletePanelTagsRequest:{serialNumber:"%s",tagId:"%s"})
}
                   """
        response = self.send_query(query % (serialNumber, tagId))
        body = json.loads(response.text)
        return response, body

    def executeAppInstall(self, serialNumbers, url):
        query = """
mutation executeAppInstall {
    executeAppInstall(appInstallRequest:{serialNumbers:"%s",url:"%s"}) {
        result
    }
}
        """
        response = self.send_query(query % (serialNumbers, url))
        body = json.loads(response.text)
        return response, body

    def enroll(self, SN, panelName, showprint=True):
        query = """
mutation enroll {
  enroll(input: [{ serialNumber: "%s", panelName: "%s" }]) {
    serialNumber
    panelName
    error
    enrolled
  }
}
                """
        response = self.send_query(query % (SN, panelName), showprint=showprint)
        body = json.loads(response.text)
        return response, body

    def unenroll(self, SN, showprint=True):
        query = """
mutation unenroll {
  unenroll(
    serialNumbers: "%s"
  ) {
    serialNumber
    unenrolled
    error
  }
}
                """
        response = self.send_query(query % SN, showprint=showprint)
        body = json.loads(response.text)
        return response, body
# ----------------MUTATIONS End ----------------

# ----------------configuration Query ----------------
# QUERIES:

    def configurationList(self, pageNumber, pageSize, showprint=True):
        query = """
query configurationList{
configurationList(input:{pageNumber:%d,pageSize:%d}){
        configurations{
            configurationId
            name
            description
            orgId
            createBy
            createTime
            updateTime
            appliedPanels
            failedInstalls
        }
        total
    }
}
"""

        response = self.send_query(query % (pageNumber, pageSize), showprint=showprint,
                                   api='configuration')
        body = json.loads(response.text)
        return response, body

    def configurationDetail(self, configurationId, showprint=True):
        query = """
query configurationDetail{
configurationDetail(configurationId: "%s"){
      configurationId
      name
      description
      orgId
      createBy
      createTime
      updateTime
      appliedPanels
      failedInstalls
  }
}
            """
        response = self.send_query(query % configurationId, showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body

    def createConfiguration(self, name, description, showprint=True):
        query = """
mutation{
createConfiguration(input:{name:"%s", description:"%s"}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
        """
        response = self.send_query(query % (name, description), showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body

    def updateConfiguration(self, configurationId, name, description, showprint=True):
        query = """
mutation{
updateConfiguration(configurationId:"%s",
    input:{name:"%s", description:"%s"}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
                """
        response = self.send_query(query % (configurationId, name, description),
                                   showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body

    def deleteConfiguration(self, configurationId, showprint=False):
        query = """
mutation{
    deleteConfiguration(configurationId:"%s"){
    success
    }
}
        """
        response = self.send_query(query % configurationId, showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body

    def updateConfigurationPayload(self, configurationId, frequency, dayOfWeek, time, showprint=True):
        query = """
mutation{
  updateConfigurationPayload(configurationId:"%s",input:{
    configKey:"power",
    configPayload:{
      autoOff:{
                frequency:"%s"
                dayOfWeek:%d
                time:"%s" 
      }
    }
  })
{
  configKey,
  configPayload,
}
}
"""
        response = self.send_query(query % (configurationId, frequency, dayOfWeek, time),
                                   showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body

    def getDeployConfig(self, serialNumber, showprint=True):
        query = """
query{
  getDeployConfig(getDeployConfigRequest:{serialNumber:"%s"}){
    configurationId,
    configurationName,
    description,
    createBy,
    orgId,
    createTime,
    updateTime,
    status,
    appliedPanels,
    failedInstalls,
    isUnique,
    deployStatus,
    deploymentTime,
    configurationPayload,
  }
}
                """
        response = self.send_query(query % serialNumber, showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body

    def getAppliedPanel(self, configurationId, showprint=True):
        query = """
query{
 getAppliedPanel(getDeployPanelRequest:{configurationId:"%s"}){
   panels{
    serialNumber,
    panelName,
  }
  }
}
        """

        response = self.send_query(query % configurationId, showprint=showprint, api='configuration')
        body = json.loads(response.text)
        return response, body
