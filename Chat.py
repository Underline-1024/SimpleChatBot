import requests
import json
import text2speach
import random
import string
from tavily import TavilyClient
import functioncalling
from pysenti import ModelClassifier
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
def get_search(searching_content:str)->dict:
    tavily_client=TavilyClient(api_key="Your Key")
    return tavily_client.search(searching_content,include_images=True,include_answer=True)

datas=[]
with open("data.json","r",encoding="utf-8") as f:
    datas=json.loads(f.read())
url='http://localhost:11434/api/chat'
input_data=input("please input：")
while input_data!="#exit":
    post_message=json.dumps({
        "model":"llava",
        "messages":datas+[
            {
                "role":"user",
                "content":f"{input_data}##emotional_tendency:{ModelClassifier().classify(input_data)}",
                "images":None
            }
        ],
        "stream":False
    })
    datas.append(json.loads(post_message)["messages"][-1])#
    post=requests.post(url,post_message)
    while post.status_code!=200:
        post=requests.post(url,post_message)
    reply_content=json.loads(post.text)["message"]
    datas.append(reply_content)
    if "##function\_calling" in reply_content["content"]:
        args=functioncalling.ToolCall(get_search).calling(reply_content["content"].replace("##function_calling",""))
        if args!=[]:
            search_result=get_search(args[0]["args"]["searching_content"])["answer"]
            post_message=json.dumps({
                "model":"Your function_calling model",
                "messages":datas+[
                    {
                        "role":"system",
                        "content":"##returned_result:"+search_result,
                        "images":None
                    }
                ],
                "stream":False
            })
            datas.append(json.loads(post_message)["messages"][-1])#
            print("datas:"+str(datas))
            post=requests.post(url,post_message)
    print(json.loads(post.text)["message"]["content"])

    t2s=text2speach.Text2Speech()
    t2s.text2speech(text=json.loads(post.text)["message"]["content"],file_name="soundfile")

    datas.append(json.loads(post.text)["message"])
    input_data=input("please input：")
with open("data.json","w",encoding="utf-8") as f:
    f.write(json.dumps(datas))
