import json
import requests
from prome_lib import Response
import unittest

class BatchBackendEnroll(unittest.TestCase):
    def setUp(self):
        self.base_proxies = {
            'http': 'http://127.0.0.1:1080',
            'https': 'http://127.0.0.1:1080'
        }
        token = Response.get_token()
        self.token = json.loads(token)
        self.headers = {'Content-Type': 'application/json'}
        # add token to headers
        self.headers.update(self.token)
        self.serialNumber = "65W25KCI18CX135000017P"
        self.PaenlName = "65W25KCI18CX135000017P"
        self.enroll_url = "https://sandboxapi.prometheanproduct.com/mdm/devices"
        self.enroll_payload = '''{"enrollmentInfo":[{"serialNumber":"65W25KCI18CX135000017P",
                                                    "panelName":"65W25KCI18CX135000017P"}]}'''
        self.unenroll_url = "https://sandboxapi.prometheanproduct.com/mdm/devices?serialNumbers=%s" % self.PaenlName

    def test_enroll_unenroll(self):
        def test(i):
            print "\n----------- %d test times -----------" % (i + 1)
            enroll_r = requests.patch(url=self.enroll_url, proxies=self.base_proxies,
                                      headers=self.headers, data=self.enroll_payload)
            enroll_body = json.loads(enroll_r.text)
            print "enroll status code:", enroll_r.status_code
            print 'enroll query: \n ', self.enroll_payload
            print '\nenroll response: \n', json.dumps(enroll_body, indent=4, sort_keys=True)
            print '\n'
            if enroll_body[0]["error"] == "Panel already enrolled":
                requests.delete(url=self.unenroll_url, proxies=self.base_proxies, headers=self.headers)
                return test(i)
            else:
                self.assertEqual(enroll_r.status_code, 200)
                self.assertEquals(enroll_body[0]["serialNumber"], self.serialNumber)
                self.assertIsNone(enroll_body[0]["error"])
                self.assertEquals(enroll_body[0]["panelName"], self.PaenlName)

            # unenroll
            unenroll_r = requests.delete(url=self.unenroll_url, proxies=self.base_proxies, headers=self.headers)
            print "unenroll status code: ", unenroll_r.status_code
            unenroll_body = json.loads(unenroll_r.text)
            print 'unenroll response :\n', json.dumps(unenroll_body, indent=4, sort_keys=True)
            print '\n----------------- End -----------------\n'
            self.assertEqual(unenroll_r.status_code, 200)
            self.assertEquals(unenroll_body[0]["serialNumber"], self.serialNumber)
            self.assertIsNone(unenroll_body[0]["error"])
            self.assertEquals(unenroll_body[0]["unenrolled"], True)

        for i in range(666):
            test(i)

# if __name__ == '__main__':
#     unittest.main()

