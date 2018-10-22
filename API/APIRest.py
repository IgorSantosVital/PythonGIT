import json, requests

response = requests.get("http://jsonplaceholder.typicode.com/comments/1")
print(response.status_code)
print(response.content)
comments = json.loads(response.content)
print(comments)
print(comments['name'])

