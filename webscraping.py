import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    for heading in soup.find_all("h1"):
        print(heading.text.strip())
else:
    print("Failed to retrieve the webpage.")