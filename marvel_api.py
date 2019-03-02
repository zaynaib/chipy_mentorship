import requests
from requests.auth import HTTPBasicAuth
import json




hash <- digest(paste0(ts, privateKey, publicKey), algo="md5")


#url = 'http://gateway.marvel.com/v1/public/characters?ts=1&apikey=4b6b320a8f9ed5098d9da60656994c65'
public_key = '4b6b320a8f9ed5098d9da60656994c65'
private_key = '317d2da9b251d0524fac47b7864e3dbd4f6d7ecf'
timeStamp =d
url = 'http://gateway.marvel.com/v1/public/comics'

r = requests.get(url, auth=HTTPBasicAuth(api_token))
print(r)

#requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))

