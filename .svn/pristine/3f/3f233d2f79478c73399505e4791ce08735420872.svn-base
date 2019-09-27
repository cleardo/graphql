# coding=utf-8
from nd.rest.co_http.co_curl import Http

Http.DEBUG = True

from prome_lib.graphql_query import mainclass


class Device(object):
    def __init__(self, name):
        self.name = name
        host = "sandboxapi.prometheanproduct.com"
        self.graphql = mainclass()
        token = self.graphql.api_token
        self.http_o = Http(host, ssl=True)

        headers = {}
        headers['Accept'] = "application/json"
        headers['Content-Type'] = "application/json"
        headers['x-api-key'] = ""
        headers['Authorization'] = "Bearer " + token.encode("utf-8")

        self.http_o.set_header(headers)
        pass

    def delete(self):
        url = "/iot-maint/device/" + self.name
        self.http_o.delete(url)


    def checkin



if __name__ == "__main__":
    dev = Device("65W25KCI18CX135000017P")
    dev.delete()