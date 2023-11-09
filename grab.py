import requests
import re
import os

# coded by #No_Identity 
# Copyright xReverseLabs - Linuxploit.com
# https://t.me/xxyz4
# join channel : https://t.me/exploi7

def grab_domains_by_date(date, page):
    url = f"https://api.xreverselabs.my.id/apibydate_public?date={date}&page={page}"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return []

    rex = re.findall(r'<br>(.*?)<br>', response.text)
    return rex

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = """
    
░██████╗░██████╗░░█████╗░██████╗░██████╗░░█████╗░████████╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║░░██╗░██████╔╝███████║██████╦╝██║░░██║███████║░░░██║░░░█████╗░░
██║░░╚██╗██╔══██╗██╔══██║██╔══██╗██║░░██║██╔══██║░░░██║░░░██╔══╝░░
╚██████╔╝██║░░██║██║░░██║██████╦╝██████╔╝██║░░██║░░░██║░░░███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

Coded by #No_Identity - https://t.me/xxyz4
Join : https://t.me/exploi7
    """
    print(banner)
    date = input("Date (format: YYYY-MM-DD) > ")
    page = 1

    all_domains = set()
    while True:
        print(f"Processing page {page}...")
        domains = grab_domains_by_date(date, page)
        print("Domains:", domains)
        if not domains:
            break

        new_domains = set(domains) - all_domains
        print("New Domains:", new_domains)
        if not new_domains:
            print("No new domains found. Stopping.")
            break

        all_domains.update(new_domains)
        page += 1

    if all_domains:
        print(f"Results for {date}:")
        for domain in all_domains:
            print(f"-| {domain}")
            open(f"Domain-{date}.txt", 'a').write('http://' + domain + '\n')
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
