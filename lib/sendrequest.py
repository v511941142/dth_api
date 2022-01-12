import requests


class SendRequest:
    def sendGet(self, url, data, headers=None):
        res = requests.get(url=url, params=data, headers=headers)
        return res

    def sendPost(self, url, data, headers=None):
        res = requests.post(url=url, data=data, headers=headers)
        return res

    def sendRequest(self, method, url, data, headers):
        if method.upper() == 'GET':
            res = self.sendGet(url, data, headers)
        elif method.upper() == 'POST':
            res = self.sendPost(url, data, headers)
        return res.json()


if __name__ == '__main__':
    s = SendRequest()
    method = 'post'
    url = 'http://223.75.245.243:9089/gaea/v1/user/login.json'
    data = {"passWord": "a123456", "userName": "15500000002"}
    headers = ''
    res = s.sendRequest(method, url, data, headers)
    print(res['status'])
    print(res['message'])
