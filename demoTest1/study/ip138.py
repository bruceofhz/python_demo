import requests

url = 'http://www.ip138.com/ip.asp?ip='

ip = '139.162.86.48'
r = requests.get(url + ip)
print(r.status_code)
print(r.text[-500:])
