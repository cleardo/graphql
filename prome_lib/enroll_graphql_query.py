# coding=utf-8

import json
import os
import csv
from data_struct import batch_enroll_data
from graphql_query import GraphqlQuery


# 注册模块 EnrollModuel
class EnrollModuel(GraphqlQuery):

    # 注册Panel,    New Enroll Panel.
    def enroll(self, serialNumber, panelName):
        enroll = """
        mutation {
            enroll(input: [{serialNumber: "%s", panelName: "%s"}])
            {
            enrolled,
            error,
            }
        }
        """
        response = self.send_query(enroll % (serialNumber, panelName))
        body = json.loads(response.text)
        print (enroll)
        return response, body

    # 验证已注册Panel,    verify enrolled Panel.
    def enroll_validation(self, serialNumber, panelName=""):

        query = """
                {
                    EnrollValidation(input: [{serialNumber: "%s", panelName: "%s"}])
                    {
                    isValid,
                    error,
                    }
                }
                """
        query = query % (serialNumber, panelName)
        response = self.send_query(self.url, query, self.headers)
        body = json.loads(response.text)
        # print (query)
        return response, body

    # 解除已注册Panel,   unenroll enrolled Panel.
    def unenroll(self, serialNumbers):
        unenroll = """
        mutation {
          unenroll(serialNumbers:"%s")
          {
          unenrolled,
          error,
          }
        }
        """
        response = self.send_query(self.url, unenroll % (serialNumbers), self.headers)
        body = json.loads(response.text)
        return response, body

    # 批量注册面板,   batch enroll Panel.
    def batch_enroll(self,filename):
        final_string = ""
        dir = os.path.dirname(os.path.abspath(batch_enroll_data.REPORT_DIR))  # 获取csv文件的路径
        data_filename = os.path.join(dir, filename)  # 获取csv文件
        with open(data_filename) as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:  # 循环读取每行数据

                sn_data = row[0]  # 每行的第1个数值复制给sn
                name_data = row[1]  # 每行的第2个数值复制给name
                json_string = "{serialNumber: \"%s\",panelName: \"%s\"}" % (sn_data, name_data)  # 拼成需要的格式
                if final_string:  # 判断是否为空
                    final_string = "{},{}".format(json_string, final_string)  # 不为空就拼接字符串
                else:
                    final_string = json_string  # 为空则赋值

        enroll = """
                mutation{
                    enroll(input: [%s])
                            {
                            enrolled,
                            error,
                            }
                        }
                        """
        enroll = enroll % (final_string)
        response = self.send_query(self.url, enroll, self.headers)
        body = json.loads(response.text)
        # print (enroll)
        return response, body

    # 批量验证已注册面板,    batch verify enrolled Panel.
    def batch_enroll_validation(self, filename):
        final_string = ""
        dir = os.path.dirname(os.path.abspath(batch_enroll_data.REPORT_DIR))  # 获取csv文件的路径
        data_filename = os.path.join(dir, filename)  # 获取csv文件
        with open(data_filename) as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:  # 循环读取每行数据

                sn_data = row[0]  # 每行的第1个数值复制给sn
                name_data = row[1]  # 每行的第2个数值复制给name
                json_string = "{serialNumber: \"%s\",panelName: \"%s\"}" % (sn_data, name_data)  # 拼成需要的格式
                if final_string:  # 判断是否为空
                    final_string = "{},{}".format(json_string, final_string)  # 不为空就拼接字符串
                else:
                    final_string = json_string  # 为空则赋值

        query = """
        {
            EnrollValidation(input: [%s])
                    {
                    isValid,
                    error,
                    }
                }
                """
        query = query % (final_string)
        response = self.send_query(self.url, query, self.headers)
        body = json.loads(response.text)
        # print (query)
        return response, body

    # 批量解除已注册Panel,     batch unenroll enrolled Panel.
    def batch_unenroll(self,filename):
        final_string = ""
        dir = os.path.dirname(os.path.abspath(batch_enroll_data.REPORT_DIR))  # 获取csv文件的路径
        data_filename = os.path.join(dir, filename)  # 获取csv文件
        with open(data_filename) as f:
            csv_reader = csv.reader(f)
            for sn in csv_reader:
                sn_data = sn[0]
                json_string = "\"%s\"" % (sn_data)
                if final_string:
                    final_string = "{},{}".format(json_string, final_string)
                else:
                    final_string = json_string
        # print final_string
        unenroll = """
                                mutation{
                                    unenroll(serialNumbers: [%s])
                                            {
                                            unenrolled,
                                            error,
                                            }
                                        }
                                        """
        unenroll = unenroll % (final_string)
        response = self.send_query(self.url, unenroll, self.headers)
        body = json.loads(response.text)
        print unenroll
        return response, body
