import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from filterLinks import is_valid_url,isUseFullLink
from savedata import save_webpage_to_pdf

def get_html_content(html_file_url):
    try:
        if html_file_url.startswith('http'):
            return requests.get(html_file_url).text
        else:
            with open(html_file_url, 'r', encoding='utf-8') as file:
                return file.read()
    except Exception as e:
        print(f"Error reading '{html_file_url}': {str(e)}")
        return None    
       
def get_links(soup, html_url, links_set, markdowns):
    for link in soup.find_all('a'):
        href = link.get('href')
        hyperlink = contsruct_full_url(href, get_base_url(url=html_url))
        if hyperlink is None or not is_valid_url(hyperlink) or not isUseFullLink(hyperlink):
            continue
        if hyperlink not in links_set and hyperlink.startswith(get_base_url(html_url)):
            add_link(hyperlink, links_set)
            read_webpage(html_url=hyperlink,  links_set=links_set, markdowns=markdowns)

def get_markdown(soup):
    markdown_content = html2text.html2text(str(soup))
    return markdown_content

def read_webpage(html_url, links_set, markdowns):
    html_content = get_html_content(html_url)
    if html_content is None:
        return
    soup = BeautifulSoup(html_content, 'html.parser')
    md_content = get_markdown(soup)
    markdowns.append(md_content)
    get_links( html_url=html_url, soup=soup, links_set=links_set, markdowns=markdowns)

def get_base_url(url):
    # Parse the URL into its components
    parsed_url = urlparse(url)
    
    # Reconstruct the URL with only the scheme, netloc (hostname), and port
    base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    
    return base_url

def contsruct_full_url(href, base_url):
    if href is None or href.startswith('#') or href == '/' or href == '' or href == './':
        return None
    elif href.startswith('http') or href.startswith('https') or href.startswith('www'):
        return href
    elif href.startswith('/'):
        return base_url + href
    elif href.startswith('./'):
        return base_url + href[1:]
    else:
        return base_url + href

def add_link(link, links_set):
    if link not in links_set:
        links_set.add(link)



