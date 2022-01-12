import requests
import jsonpath

url = 'http://223.75.245.243:9089/gaea/v1/user/login.json'
data = {"passWord": "a123456", "userName": "15500000002"}

res = requests.post(url=url, data=data).json()
json_path = {'$.status': 200, '$.message': 'success', '$.data.userName': '15500000002','$.data.name': '黄文琪'}

for k, v in json_path.items():
    r = jsonpath.jsonpath(res, k)[0]
    print(r,v)
    print(r==v)