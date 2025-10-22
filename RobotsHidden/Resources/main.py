import requests
import json
from bs4 import BeautifulSoup

def recursive_autolist(url: str):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    links = [a['href'] for a in soup.find_all('a', href=True)]
    links = [link for link in links if link not in ("../", "./")]

    if links == ["README"]:
        readme_content = requests.get(f"{url}/README").text
        print(readme_content)
        return None

    for link in links:
        recursive_autolist(f"{url}/{link}")

host = "darkly"
url = f"http://{host}/.hidden"

root_raw_html = requests.get(url).text
root_soup = BeautifulSoup(root_raw_html, "html.parser")

links = [a['href'] for a in root_soup.find_all('a', href=True)]
links = [link for link in links if link not in ("README", "../", "./")]

for link in links[:-1]:
    recursive_autolist(f"{url}/{link}")
    # print("================ AAAAAAAAAAAAAAAAAAAAAAA ======================")

