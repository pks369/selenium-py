import requests 
import  json
import  jsonpath

# API URL
url="https://reqres.in/api/users";
    
#read input json file
# file=open("C://Users//Dell//PycharmProjects//selenium//API Testing//user_post.json//user_post.json",'r')
json_input='{"name":"pappu","desination":"sr software engineer","from":"india"}'
# json_input=file.read()   
request_json=json.loads(json_input)
#make post request with json input body
response=requests.post(url,request_json)
print(response.content)

#validating response code # 202 False
assert response.status_code==201

# fetch header from response
# print(response.headers)

# fetch header content length

print(response.headers.get('content-length'))

 #parse response to json formate
response_json=json.loads(response.text)
 #pick id using  json path
id=jsonpath.jsonpath(response_json,'id')
print(id[0])