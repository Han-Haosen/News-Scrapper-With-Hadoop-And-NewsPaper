import pyhdfs
import custom_b
import json
import random
def run(result):
    jsonName = random.randint(0,1000000)
    hdfsclient = pyhdfs.HdfsClient('192.168.137.2:50070',user_name="root")
    print(hdfsclient.listdir("/newsData/test"))
    hdfsclient.mkdirs("/newsData/result")
    tempObject = {
        "url":result.temp_url,
        "html":result.html,
        "text":result.text,
        "time":result.temp_time,
        "images":result.temp_image_links
    }
    with open(str(jsonName) + "news.json","w") as writeJson:
        json.dump(tempObject,writeJson)
        hdfsclient.copy_from_local("./" + str(jsonName) + "news.json", "/newsData/result/"+ str(jsonName) + "news.json")



