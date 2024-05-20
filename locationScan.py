import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            print(f"message is {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: {e} The URL is: {url}")
        return None

def find_others(html, urls, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    nav_items = soup.find('ul', class_='Navigation-items')
    if not nav_items:
        return

    links = nav_items.find_all('a')
    link_urls = [link.get('href') for link in links if link.get('href')]
    for link in link_urls:
        find_end(urls, link, base_url)

def find_end(urls, url, base_url):
    full_url = urljoin(base_url, url)

    if ("https://www.byui.edu/financial-aid/" in url
    or "http://www.byui.edu/financial-aid/" in url
    or "https://www.byui.edu/financial-services/" in url) and "#" not in url:
        if full_url not in urls:
            urls.add(full_url)  # Use set instead of list
            soup = BeautifulSoup(get_page(full_url), 'html.parser')

            # Find the main element with class 'Page-main'
            #main_content = soup.find('main', class_='Page-main')
            #if not main_content:
            #    print("No 'main.Page-main' section found")
            #    return

            # Find all <a> tags within this main element
            links = soup.find_all('a')
            link_urls = [link.get('href') for link in links if link.get('href')]
            for link in link_urls:
                find_end(urls, link, base_url)
    else:
        print(f"Outbound site / site already in list: {url}")

def main():
    print("Scanning...")
    urls = set()  # Use set to store unique URLs
    
    base_url = 'https://www.byui.edu/financial-aid/'
    
    page_content = get_page(base_url)
    if page_content:
        find_end(urls, base_url, base_url)
        print(urls)
    
        with open('locations.txt', 'w') as f:
            for url in urls:
                f.write(f"{url}\n")

if __name__ == '__main__':
    main()

