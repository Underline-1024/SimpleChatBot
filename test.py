import requests
import json
content=json.dumps({
                    "appId": 102090954,
                    "clientSecret": "0aAkKuU4fGrS3eFrT5hJvXAnQ3gJwaEs",
                },)
print(requests.get("https://bots.qq.com/app/getAppAccessToken",data="").text)