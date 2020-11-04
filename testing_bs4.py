import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
res = requests.get("https://www.amazon.com.br/Automate-Boring-Stuff-Python-Programming/dp/1593275994", headers=headers)
print(res.raise_for_status())
soup = bs4.BeautifulSoup(res.text, "html.parser")
soup.select("#soldByThirdParty > span")
