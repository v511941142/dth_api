import jsonpath


class AssertResult():
    def assertEqual(self, result, jsonList):
        isEqual = True
        for json_path, expect_value in jsonList.items():
            res = jsonpath.jsonpath(result, json_path)[0]
            if res != expect_value:
                isEqual = False
        return isEqual


if __name__ == '__main__':
    import requests

    url = 'http://223.75.245.243:9089/gaea/v1/user/login.json'
    data = {"passWord": "a123456", "userName": "13011111111"}
    res = requests.post(url=url, data=data).json()
    json_path = {'$.status': 500, '$.message': 'exception', '$.data[*].errorMessage': '用户名或密码错误，请仔细检查后重新登录',
             '$.data[*].nodesName[0]': 'publicError'}

    a = AssertResult()
    r = a.assertEqual(res, json_path)
    print(r)