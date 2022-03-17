# Demo of consuming Github API using python

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

## Use GET to get details about the specified user 
```
response = requests.get("https://api.github.com/users/aishwaryasarath", headers=headers)
print(response.json)
```

## GET own info without specifying username in API
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

## Use POST to create a new repo and output the status code
```
payload = {"name": "test_repo_python_API_POST"}
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)
```

## Use PATCH to update the repo description and output the status code
```
payload = {"description": "Creating a repo using github API", "name": "test_repo_python_API_POST"}
response = requests.patch("https://api.github.com/repos/aishwaryasarath/test", json=payload, headers=headers)
print(response.status_code)
```

## Use DELETE to delete the repo and output the status code
```
response = requests.delete("https://api.github.com/repos/aishwaryasarath/test_repo_python_API_POST", headers=headers)
print(response.status_code)
```
