import requests
from proxypool.setting import TEST_URLs

proxy = '223.199.24.25:9999'

# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy,
# }
proxies = {'http': proxy}

print(TEST_URLs[0])
response = requests.get(TEST_URLs[0], proxies=proxies)
if response.status_code == 200:
    print('Successfully')
    print(response.headers)
    print(response.content.decode('utf8'))
