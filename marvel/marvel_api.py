import requests
import json
import datetime
import hashlib
from config import *



time_stamp = str(datetime.datetime.now().timestamp())
hash_key = time_stamp +private_key + public_key
hash_key_algo = hashlib.md5(hash_key.encode() )
result_hash = hash_key_algo.hexdigest()

url = 'http://gateway.marvel.com/v1/public/comics?' + 'ts=' +time_stamp + '&apikey=' + public_key + '&hash=' + str(result_hash)
print(url)

response = requests.get(url)
print(response)


