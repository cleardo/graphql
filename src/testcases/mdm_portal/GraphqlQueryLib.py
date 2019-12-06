# coding=utf-8
from src.lib.queryGraphql import *

api = 'mdm-portal'

"""
以下为mdm-portal.queries模块封装的函数
"""


def queryPanels(pageSize, offset, showprint=True):
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
        }totalCount
    }
}
    """ % (pageSize, offset)
    return queryGraphql(query, api, showprint)


def queryPanel(serialNumber, showprint=True):
    query = """
query getPanelBySN{
    Panel(serialNumber:"%s"){
        summary{name, serialNumber}
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
    """ % serialNumber
    return queryGraphql(query, api, showprint)


def queryTags(showprint=True):
    query = """
query{
    Tags{
        group,
        values{id,value}
    }
}
    """
    return queryGraphql(query, api, showprint)


def queryOta(showprint=True):
    query = """
    query{
    Ota{version, notes}
}
    """
    return queryGraphql(query, api, showprint)


def queryActivityLogs(serialNumber, profileIds="", pageSize=1, offset=0, showprint=True):
    query = """
query {
    ActivityLogs(searchActivityLog: {serialNumber:"%s", profileIds:"%s", pageSize:%s, offset:%s})
    {totalCount,
        logs{
          createTime,
          user,
          panelName,
          eventDetail,
          event,
          organization,
          status,
          serialNumber
        }
    }
}
            """ % (serialNumber, profileIds, pageSize, offset)
    return queryGraphql(query, api, showprint)


def queryModelList(showprint=True):
    query = """
query ModelList{
    ModelList
}
    """
    return queryGraphql(query, api, showprint)


def queryMainboardFirmwareList(showprint=True):
    query = """
query MainboardFirmwareList {
MainboardFirmwareList
}
    """
    return queryGraphql(query, api, showprint)


def queryUserList(showprint=True):
    query = """
query {
  UserList {
    user
    profileId
  }
}
    """
    return queryGraphql(query, api, showprint)


def queryDeployInfo():
    pass


def queryEnrollValidation(serialNumber, panelName, showprint=True):
    # 废弃接口 不测
    pass


"""
以下为mdm-portal.queries模块封装的函数
"""


def queryUpdatePanelName(serialNumber, name, showprint=True):
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
        """ % (serialNumber, name)
    return queryGraphql(query, api, showprint)


def queryCreateTag(group, tagname, showprint=True):
    query = """
mutation createTag {
createTag(group: "%s", value:"%s") {
    id
    value
    group
}
}
            """ % (group, tagname)
    return queryGraphql(query, api, showprint)


def queryDeleteTag(tagid, showprint=True):
    query = """
mutation deleteTagById{
    deleteTag(id:"%s"){
        id,
        group,
        value
    }
}
    """ % tagid
    return queryGraphql(query, api, showprint)


def queryUpdateTag(tagid, group, value, showprint=True):
    query = """
mutation {
    updateTag(id:"%s", group:"%s", value:"%s") {
        id,
        group,
        value
    }
}
        """ % (tagid, group, value)
    return queryGraphql(query, api, showprint)


def queryExecuteOta(SNList, showprint=True):
    query = """
mutation {
executeOta(serialNumberList:"%s")
}
           """ % SNList
    return queryGraphql(query, api, showprint)


def queryAddpanelTags(serialNumber, tagId, showprint=True):
    query = """
mutation{
    addPanelTags(addPanelTagsRequest:{serialNumber:"%s",tagId:"%s"})
}
                """ % (serialNumber, tagId)
    return queryGraphql(query, api, showprint)


def queryUpdatepanelTags(serialNumber, tagId, showprint=True):
    query = """
mutation{
updatePanelTags(updatePanelTagsRequest:{serialNumber:"%s",tagId:"%s"})
}
               """ % (serialNumber, tagId)
    return queryGraphql(query, api, showprint)


def queryDeletePanelTags(serialNumber, tagId, showprint=True):
    query = """
mutation{
deletePanelTags(deletePanelTagsRequest:{serialNumber:"%s",tagId:"%s"})
}
               """ % (serialNumber, tagId)
    return queryGraphql(query, api, showprint)


def queryExecuteAppInstall(serialNumbers, url, showprint=True):
    query = """
mutation executeAppInstall {
executeAppInstall(appInstallRequest:{serialNumbers:"%s",url:"%s"}) {
    result
}
}
    """ % (serialNumbers, url)
    return queryGraphql(query, api, showprint)


def queryCommand():
    pass


def queryListUpload():
    # 开发自用接口，不测
    pass


def queryEnroll(SN, panelName, showprint=True):
    query = """
mutation enroll {
    enroll(input: [{ serialNumber: "%s", panelName: "%s" }]) {
        serialNumber
        panelName
        error
        enrolled
    }
}
            """ % (SN, panelName)
    return queryGraphql(query, api, showprint)


def queryUnenroll(SN, showprint=True):
    query = """
mutation unenroll {
    unenroll(serialNumbers: "%s") {
    serialNumber,
    unenrolled,
    error
    }
}
            """ % SN
    return queryGraphql(query, api, showprint)
