
import requests
import json
#token generated from github developers setting
headers = {"Authorization": "token ******"}

# Make a GET request to the GitHub API with our headers.
print("Start of GET demo using token\n")
# This API endpoint will give us details about the user aishwaryasarath.
response = requests.get("https://api.github.com/users/aishwaryasarath", headers=headers)
print(response.json())
print("End of GET\n")

# display info of other users
print("Start of GET info of other users\n")
response = requests.get("https://api.github.com/users/torvalds", headers=headers)
torvalds = response.json()
print("End of GET info of other users\n")

# repo owned by other user
print("Start of GET repo of other user\n")
response = requests.get("https://api.github.com/repos/octocat/Hello-World", headers=headers)
hello_world = response.json()
print(hello_world)
print("END of GET repo of other user\n")

# limiting pages
print("Start of Limiting the page and info/page displayed\n")
params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/aishwaryasarath/starred", headers=headers, params=params)
page1_repos = response.json()
print(page1_repos)
print("End of Limiting the page and info/page displayed\n")

# Getting our own info. Since we have authenticated, we dont need to specify our username.
print("Start of getting our own info without specifying the user details\n")
response = requests.get("https://api.github.com/user", headers=headers)
user = response.json()
print("End of getting our own info without specifying the user details\n")


# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
print("Start of POST \n")
payload = {"name": "test_repo_python_API_POST"}
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)
print("End of POST \n")

###############PATCH############
print("Start of PATCH\n")
payload = {"description": "Creating a repo using github API", "name": "test_repo_python_API_POST"}
response = requests.patch("https://api.github.com/repos/aishwaryasarath/test", json=payload, headers=headers)
print(response.status_code)
print("End of PATCH\n")

###############DELETE######
print("Start of DELETE\n")
response = requests.delete("https://api.github.com/repos/aishwaryasarath/test_repo_python_API_POST", headers=headers)
print(response.status_code)
print("Start of DELETE\n")
