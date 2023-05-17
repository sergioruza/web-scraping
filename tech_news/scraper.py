import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    posts_url = []
    for link in selector.css(".entry-title a::attr(href)"):
        posts_url.append(link.get())
    return posts_url


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()
    return next_page


def scrape_news(html_content):
    selector = Selector(text=html_content)

    title = selector.css("h1.entry-title::text").get()
    reading_time = (
        selector.css("li.meta-reading-time::text").get().split(" ")[0]
    )
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary)
    category = selector.css(".label::text").get()

    return {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": title.rstrip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "reading_time": int(reading_time),
        "summary": summary.rstrip(),
        "category": category.strip(" "),
    }


def get_tech_news(amount):
    BASE_URL = "https://blog.betrybe.com/"
    news_list = []

    while len(news_list) < amount:
        html_content = fetch(BASE_URL)
        for url in scrape_updates(html_content):
            html = fetch(url)
            news = scrape_news(html)
            news_list.append(news)

        next_page = scrape_next_page_link(html_content)
        BASE_URL = next_page

    print(news_list[0])
    create_news(news_list)
    return news_list
