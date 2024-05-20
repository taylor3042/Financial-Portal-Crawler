import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch page: {e} The URL is: {url}")
        return None

def findOthers(html, urls):
    print('got to this point')
    soup = BeautifulSoup(html, 'html.parser')
    navItems = soup.select_one("#Navigation-items-item")
    print(navItems)
    



def findEnd(urls):
    for url in urls:
        if "CategoryID" in url:
            findOthers(get_page(url), urls)  
            # Recursion to loop back until there's no more links to change folder location.
        elif "ArticleDet" in url:
            findEnd.append(url)
        else:
            print("ERROR!")


def exceptions(links):
    exception = str(links).strip()
    if(exception != "Expand" and exception is not None):
        #I'm leaving this open to find more exception to have under the tag I found that work for catagories.
        return True
    else:
        return False


def main():
    print("Using shallow scan...")
    urls = []
    
    starting_path = 'https://www.byui.edu/financial-aid/'
    findOthers(get_page(starting_path), urls)
    findEnd(urls)
    
    with open('locations.txt', 'w') as f:
        for url in urls:
            f.write(f"{url}\n")

if __name__ == '__main__':
    main()
