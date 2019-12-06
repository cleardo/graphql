# coding=utf-8
from src.setting.setting import *
from src.lib.getEnvInfo import *
from src.lib.getToken import *
import json
import requests
import logging


def queryGraphql(query, api, showprint=True):
    """
    :param query:         请求的Graphql语句
    :param api:           接收请求的api类型
    :param showprint:     是否显示输出
    :return:              经过字典结构的response
    """

    # 获取环境信息
    envInfo = getEnvInfo()

    # 创建headers
    headers = {"x-auth-organization-id": "",
               "Authorization": "Bearer " + getToken()}

    # 选择 graphql api
    if api == 'mdm-portal':
        # 配置portal 接口地址
        graphqlAPI = envInfo['host'] + "/mdm-portal/graphql"
    elif api == 'configuration':
        # 配置configuration 接口地址
        graphqlAPI = envInfo['host'] + "/configuration/graphql"
    else:
        logging.error("[错误] - [测试项目没有{api}接口] - [请在src.queryGraphql.py 文件中配置接口地址]".format(api=api))

    # 发送 graphql 请求
    # 屏蔽https安全提示
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url=graphqlAPI, json={'query': query},
                             headers=headers, verify=False, proxies=(PROXY and PROXY_ADDRESS))
    # 将response对象转为字典结构
    r_dict = json.loads(response.text)

    # 进行断言之前确保服务器状态码为200
    if response.status_code != 200:
        print("[request] - [query]", query)
        logging.error('[graphql请求发生错误] - [status_code={}]'.format(response.status_code))
        return print("\n[response] - [body]\n", json.dumps(r_dict, indent=4, sort_keys=True))

    if showprint:
        print("\n[request] - [query]", query)
        print("\n[response] - [body]\n", json.dumps(r_dict, indent=4, sort_keys=True))

    return r_dict


if __name__ == '__main__':
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
    response = queryGraphql(query, 'configuration')
    print(response)
