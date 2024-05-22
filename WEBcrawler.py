import requests
import csv
from bs4 import BeautifulSoup, NavigableString
from dataCleaner import main as data_clean



encountered_headers = []

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

def extract_headers(html):
    soup = BeautifulSoup(html, 'html.parser')
    header = soup.find('h1')
    if header is not None:
        return soup.find('h1').get_text().strip()
    else:
        print('Header Not Found')
        return 'Header Not Found'


def extract_paragraphs(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs_and_headers = []
    main_content = soup.find('main', class_='Page-main')
    if main_content is not None:
        for element in main_content.descendants:
            if isinstance(element, NavigableString):
                # Handle text nodes
                parent_tag = element.parent.name
                if parent_tag not in ['script', 'style']:
                    text = element.strip()
                    if text and "Contact Us" not in text and "Hours of Operation" not in text and "excluding weekly devotional" not in text:
                        paragraphs_and_headers.append(text)
            elif element.name in ['p', 'h2', 'h3', 'h4']:
                text = element.get_text(strip=True)
                if text and "Contact Us" not in text and "Hours of Operation" not in text and "excluding weekly devotional" not in text:
                    paragraphs_and_headers.append(text)

        massive_text = "    ".join(paragraphs_and_headers)
        massive_text = massive_text.replace("Â", " ")  # removes the special character Â from text.
        return massive_text
    else:
        return None


def get_urls(txtFile, urls):
    # Initialize an empty list to store the URLs
    with open(txtFile, 'r') as file:
    # Read each line in the file
        for line in file:
        # Remove any leading or trailing whitespace
            url = line.strip()
        # Add the URL to the list
            urls.append(url)
    return urls

def extract_urls_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    nav_items = soup.find('ul', class_='Navigation-items')
    if not nav_items:
        return
    else:
        links = nav_items.find_all('a')
        link_urls = [link.get('href') for link in links if link.get('href')]
        return link_urls

# Display the list of URLs
def extract_info(url):
    html = get_page(url) 
    if html is not None:
        header = extract_headers(html)
        
        # Check if header already encountered
        if header in encountered_headers and header is not "Header Not Found":
            print(f"Skipping URL {url} as it has the same header as a previous URL.")
            return None, None, None
        else:
            encountered_headers.append(header)
        
        paragraphs = extract_paragraphs(html)
        uIP = extract_urls_page(html)
        # Check if header is not None before stripping
        if header is not None:
            header = header.strip()
        if paragraphs is not None:
            paragraphs = paragraphs.strip()
        
        return header, paragraphs, uIP
    else:
        return None, None, None



def export_csv(urls, txtFile):
    with open(txtFile, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Header", "Paragraphs", "URLS in page"])
        for url in urls:
            print(url)
            header, paragraphs, uIP = extract_info(url)
            if header is not None:
                header = header.strip()
            if paragraphs is not None:
                paragraphs = paragraphs.strip()
            writer.writerow([header, paragraphs, uIP])

def main():
    
    input_file = "locations.txt"
    csvFile = "htmls.csv"
    #location()
    urls = []
    get_urls(input_file, urls)
    export_csv(urls, csvFile)
    data_clean()
    print("Finished!")
if __name__ == '__main__':
    main()
    
