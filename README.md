# Demo of Github API using python

This code uses github API and developer token to authenticate and then interact with github to GET data, to POST data, to PATCH and to DELETE.
It also shows how to limit the pages in the result.

## Requirements
```python
pip install requests
```
## Code requirements
```
import json
import requests
headers = {"Authorization": "token ******"} 
```

## GET 
```
response = requests.get("https://api.github.com/users/aishwaryasarath", headers=headers)
print(response.json)
```

## GET own info without specifying username in API, but just using headers
```
response = requests.get("https://api.github.com/user", headers=headers)
print(response.json())
```

## Limiting pages
```
params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/aishwaryasarath/starred", headers=headers, params=params)
print(response.json())
```

