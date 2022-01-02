import requests


token_yd = 'AQAAAAAFE9JKAADLW7TXSY42c0hxkWbi60UwKsE'
url = 'https://cloud-api.yandex.net/v1/disk/resources/'
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token_yd)
        }


def check_folder(name):
    params = {
        'path': name
    }
    response = requests.get(url=url, headers=headers, params=params)
    print(response.status_code)
    return response.status_code


def create_folder(name):
    params = {
        'path': name
    }
    response = requests.put(url=url, headers=headers, params=params)
    print(response.status_code)
    return response.status_code


if __name__ == '__main__':
    create_folder('test_folder')
    check_folder('test_folder')
