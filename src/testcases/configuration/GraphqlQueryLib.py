# coding=utf-8
from src.lib.queryGraphql import *

api = 'configuration'

"""
以下为configuration.queries模块封装的函数
"""


def queryConfigurationDetail(configurationId, showprint=True):
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
        """ % configurationId
    return queryGraphql(query, api, showprint)


def queryConfigurationList(pageNumber, pageSize, showprint=True):
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
        }total
    }
}
            """ % (pageNumber, pageSize)
    return queryGraphql(query, api, showprint)


def queryIsUniqueConfigName(name, showprint=True):
    query = """
query{
    isUniqueConfigName(name: "%s"){
        unique
    }
}
    """ % name
    return queryGraphql(query, api, showprint)


def queryGetDeployConfig(serialNumber, showprint=True):
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
            """ % serialNumber
    return queryGraphql(query, api, showprint)


def queryGetAppliedPanel(configurationId, showprint=True):
    query = """
query{
 getAppliedPanel(getDeployPanelRequest:{configurationId:"%s"}){
   panels{
    serialNumber,
    panelName,
  }
  }
}
            """ % configurationId
    return queryGraphql(query, api, showprint)


"""
以下为configuration.mutations模块封装的函数
"""


def queryDeployConfiguration(serialNumber, configurationId, showprint=True):
    query = """
mutation
{
    deployConfiguration(deployRequest:{
        serialNumbers:"%s",
        configurationId:"%s",
        isDelayed:true
    })
}
            """ % (serialNumber, configurationId)
    return queryGraphql(query, api, showprint)


def queryCreateConfiguration(name, description, showprint=True):
    query = """
mutation{
createConfiguration(input:{name:"%s" description:"%s"}){
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
        """ % (name, description)
    return queryGraphql(query, api, showprint)


def queryUpdateConfiguration(configurationId, name, description, showprint=True):
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
                """ % (configurationId, name, description)
    return queryGraphql(query, api, showprint)


def queryDeleteConfiguration(configurationId, showprint=True):
    query = """
mutation{
deleteConfiguration(configurationId:"%s"){
success
    }
}
            """ % configurationId
    return queryGraphql(query, api, showprint)


def queryUpdateConfigurationPayload(configurationId, configKey, configPayload, showprint=True):
    query = """
mutation{
    updateConfigurationPayload(configurationId:"%s", input:{configKey:"%s", configPayload:%s}){
        configKey,
        configPayload,
    }
}
            """ % (configurationId, configKey, configPayload)
    return queryGraphql(query, api, showprint)


def queryReapply(configurationId, showprint=True):
    query = """
mutation
{
reapply(configurationId:"%s",isDelayed:true)
}
        """ % configurationId
    return queryGraphql(query, api, showprint)