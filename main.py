import requests
import datetime as dt
import os
pixela_endpoint="https://pixe.la/v1/users"

USERNAME=os.environ["USERNAME"]
TOKEN=os.environ["TOKEN"]

GRAPH_ID="graph2"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

now=dt.datetime.now()
print(now.strftime("%Y%m%d"))

graph_config={
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "minute",
    "type":"int",
    "color": "momiji",
}

header={
    "X-USER-TOKEN":TOKEN
}


#
# response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(response.text)

post_pixel_endpoint=f"{graph_endpoint}/{GRAPH_ID}"

params={
    "date":now.strftime("%Y%m%d"),
    "quantity":"80"
}

response=requests.post(url=post_pixel_endpoint,json=params,headers=header)
print(response.text)

put_endpoint=f"{post_pixel_endpoint}/20231009"

params1={
    "quantity":"90"
}
# response=requests.put(url=put_endpoint,json=params1,headers=header)
# print(response.text)

# r=requests.delete(url=put_endpoint,headers=header)
# print(r.text)