from config import *
import requests

url = "https://comicvine.gamespot.com/api/volumes/?api_key=" + key
query_format = "&format=json&sort=name:asc&filter=name:"
query_filter = "Walking%20Dead"


query = url + query_format +query_filter

# sending get request and saving the response as response object 
response = requests.get(query) 
  
# extracting data in json format 
#data = response.json() 

print(response)
  