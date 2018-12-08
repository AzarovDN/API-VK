import requests
from urllib.parse import urlencode

app_id = '6774902'
auth_url = 'https://oauth.vk.com/authorize?'

auth_data = {
    'client_id': app_id,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.92'
}
# print(auth_url + urlencode(auth_data))

# token = '333e5d97c31a8c8b889cb975eb28e4823496d5564c0d828e657e42548fd5c8b4736e19f3b65f9fa877978'
#
# params = {
#     'access_token': token_Dima,
#     'v': '5.92',
#     'source_uid': '9897521',
#     'target_uid': '230412273'
# }
# response = requests.get('https://api.vk.com/method/friends.getMutual', params)
# print(response.json())

# params_2 = {
#     'access_token': token_Dima,
#     'v': '5.92',
#     'user_id': '230412273'
# }
# info_users = requests.get('https://api.vk.com/method/users.get', params_2)

# print(info_users.json())


class User:

    token = '333e5d97c31a8c8b889cb975eb28e4823496d5564c0d828e657e42548fd5c8b4736e19f3b65f9fa877978'

    def __init__(self, user_id):
        self.user_id = user_id

    def __and__(self, other):
        token = self.token
        params = {
            'access_token': token,
            'v': '5.92',
            'source_uid': self.user_id,
            'target_uid': other.user_id
        }
        info_users = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return info_users.json()

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


dima = User(9897521)
vika = User(230412273)

print(dima & vika, '\n')

print(dima)


