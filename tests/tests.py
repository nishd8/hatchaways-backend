import requests

print('Warning!!! make sure the server is started')

#ping test
print('Ping Test')
URL="http://127.0.0.1:5000/api/ping"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

#get posts test
print('Simple Get Posts Test')
print('------------------------------------------------------------')
URL="http://127.0.0.1:5000/api/posts?tags=tech"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

#get posts test without tags parameter
print('Get Posts Test Without Tags Parameter')
print('------------------------------------------------------------')
URL="http://127.0.0.1:5000/api/posts"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

#get posts test with invalid sort by value
print('Get Posts Test With Invalid Sort By Value')
print('------------------------------------------------------------')
URL="http://127.0.0.1:5000/api/posts?tags=tech&sortBy=ids"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

#Get Posts Test With Invalid direction Value
print('Get Posts Test With Invalid Direction Value')
print('------------------------------------------------------------')
URL="http://127.0.0.1:5000/api/posts?tags=tech&sortBy=id&direction=hshsh"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

#get posts test with ascending sort by popularity
print('Get posts test with ascending sort by popularity')
print('------------------------------------------------------------')
URL="http://127.0.0.1:5000/api/posts?tags=tech&sortBy=popularity&direction=asc"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

#get posts test with descending sort by popularity
print('Get posts test with descending sort by popularity')
print('------------------------------------------------------------')
URL="http://127.0.0.1:5000/api/posts?tags=tech&sortBy=popularity&direction=desc"
r = requests.get(url = URL)
print(r.json()) 
print('------------------------------------------------------------')

