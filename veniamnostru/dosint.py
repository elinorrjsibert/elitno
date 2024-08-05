import requests

url = 'https://example.com/api/resource'
data = {
    'key1': 'value1',
    'key2': 'value2'
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Error:', response.status_code, response.text)
