import requests

res1 = requests.get('http://www.naver.com').text
print(res1)
