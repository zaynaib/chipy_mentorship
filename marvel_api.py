import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import hashlib

#hash <- digest(paste0(ts, privateKey, publicKey), algo="md5")


#url = 'http://gateway.marvel.com/v1/public/characters?ts=1&apikey=4b6b320a8f9ed5098d9da60656994c65'
public_key = '4b6b320a8f9ed5098d9da60656994c65'
private_key = '317d2da9b251d0524fac47b7864e3dbd4f6d7ecf'
time_stamp = str(datetime.datetime.now().timestamp())
hash_key = time_stamp +private_key + public_key
print(hash_key)
hash_key_algo = hashlib.md5(hash_key.encode() )
result_hash = hash_key_algo.hexdigest()
print(result_hash)

url = 'http://gateway.marvel.com/v1/public/comics?' + 'ts=' +time_stamp + '&apikey=' + public_key + '&hash=' + str(result_hash)
print(url)

#http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
#response = requests.get(url)
#print(response)

#requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))

