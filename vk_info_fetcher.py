import os

import requests
import json
import argparse


def get_user_info(user_id, token):
    params = {
        'user_ids': user_id,
        'access_token': token,
        'v': '5.131',
        'fields': 'followers_count,subscriptions'
    }
    response = requests.get('https://api.vk.com/method/users.get', params=params)
    return response.json()


def get_followers(user_id, token):
    params = {
        'user_id': user_id,
        'access_token': token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    return response.json()


def get_subscriptions(user_id, token):
    params = {
        'user_id': user_id,
        'access_token': token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.getSubscriptions', params=params)
    return response.json()


def get_groups(user_id, token):
    params = {
        'user_id': user_id,
        'access_token': token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/groups.get', params=params)
    return response.json()


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VK User Info Fetcher")
    parser.add_argument('--user_id', type=str, default=None, help='VK User ID')
    parser.add_argument('--output', type=str, default=r'C:\result.json', help='Output JSON file')
    args = parser.parse_args()

    # Ваш токен доступа
    token = os.getenv('VK_ACCESS_TOKEN')

    if not token:
        raise ValueError("Переменная VK_ACCESS_TOKEN не найдена")
    else:
        print(f"Токен: {token}")

    user_id = args.user_id or '326621197'

    # Получаем данные
    user_info = get_user_info(user_id, token)
    followers = get_followers(user_id, token)
    subscriptions = get_subscriptions(user_id, token)
    groups = get_groups(user_id, token)

    # Собираем всё в один словарь
    result = {
        'user_info': user_info,
        'followers': followers,
        'subscriptions': subscriptions,
        'groups': groups
    }

    # Сохраняем в файл
    save_to_json(result, args.output)

    print(f"Данные успешно сохранены в {args.output}")
