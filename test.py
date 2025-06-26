import requests
import json
content=json.dumps({
                    "appId": "Your Appid",
                    "clientSecret": "Your Secret Key",
                },)
print(requests.get("https://bots.qq.com/app/getAppAccessToken",data="").text)
