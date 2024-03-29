import requests

from config import token_api, base_url


async def check_user_reg(user_id):
    headers = {"Authorization": f'Token {token_api}'}
    data = requests.get(url=base_url + f'/telegram_users/{user_id}/', headers=headers)
    response = data.json()
    if 'user_id' in response.keys():
        return response['user_id'] == user_id
    else:
        return False


async def reg_user(message):
    headers = {"Authorization": f'Token {token_api}'}
    user_id = message.from_user.id
    username = f'@{message.from_user.username}'
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    data = {
        "user_id": user_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name
    }
    r = requests.post(url=base_url + f'/telegram_users/', headers=headers, json=data)
    return r.status_code


async def unsubscribe_user(message):
    headers = {"Authorization": f'Token {token_api}'}
    user_id = message.from_user.id
    r = requests.delete(url=base_url + f'/telegram_users/{user_id}/', headers=headers)
    return r.status_code
