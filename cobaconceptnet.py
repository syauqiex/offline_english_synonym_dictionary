import requests

# obj = requests.get('http://api.conceptnet.io/c/en/example').json()
# print(obj.keys())
# print(len(obj['edges']))
# print(obj['edges'][2])

obj = requests.get('http://api.conceptnet.io/uri?language=en&text=french+toast').json()
print(obj.keys())
print(obj)