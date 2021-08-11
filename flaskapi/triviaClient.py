import requests

# the URL you wish to post to
url = 'http://localhost:3000/login'

# the data you wish to post
ye_olde_dict = {'answer': 'china'}

x = requests.post(url, data = ye_olde_dict)

print(x.text)
