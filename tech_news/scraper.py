import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        request = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        status_code = request.status_code
        if status_code == 200:
            return request.text
        return None
    except requests.exceptions.RequestException:
        pass
    return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    posts_url = []
    for link in selector.css(".entry-title a::attr(href)"):
        posts_url.append(link.get())
    return posts_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# cs-overlay-link
#   next_page = selector.css(".nav-links a::attr(href)").get()
