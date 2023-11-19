import requests
#inserting changes
r = requests.get('https://api.github.com/events')

print(r)


