import requests

# the URL you wish to post to
url = 'http://localhost:3000/login'

user_input = input("Which country invented ice cream?\n>> ")

# the data you wish to post
ye_olde_dict = {'answer': user_input}

x = requests.post(url, data = ye_olde_dict)

if x.text == "Correct!!!":
    print(x)
else:
    print("Wrong...")
