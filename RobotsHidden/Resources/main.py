import requests
import json
from bs4 import BeautifulSoup

def recursive_autolist(url: str, output_file):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    links = [a['href'] for a in soup.find_all('a', href=True)]
    links = [link for link in links if link not in ("../", "./")]

    if links == ["README"]:
        # Write README content to file with URL separator
        readme_content = requests.get(f"{url}/README").text
        output_file.write(f"=== README from {url} ===\n")
        output_file.write(readme_content)
        output_file.write("\n\n")
        output_file.flush()  # Ensure content is written immediately
        return None

    for link in links:
        recursive_autolist(f"{url}/{link}", output_file)

host = "192.168.1.144"
url = f"http://{host}/.hidden"

# Open output file to store all READMEs
with open("all_readmes.txt", "w", encoding="utf-8") as output_file:
    output_file.write("=== ALL README FILES FROM .hidden DIRECTORY ===\n\n")
    
    root_raw_html = requests.get(url).text
    root_soup = BeautifulSoup(root_raw_html, "html.parser")

    links = [a['href'] for a in root_soup.find_all('a', href=True)]
    links = [link for link in links if link not in ("README", "../", "./")]

    # print(json.dumps(links, indent=2))

    for link in links[:-1]:
        recursive_autolist(f"{url}/{link}", output_file)
        # print("================ AAAAAAAAAAAAAAAAAAAAAAA ======================")

print("All README files have been saved to 'all_readmes.txt'")
