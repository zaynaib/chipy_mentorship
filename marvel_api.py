import requests

response =requests.get('https://github.com/zaynaib')
print('This response is from github', response.status_code)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
