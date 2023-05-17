from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    title_insensitive = {"$regex": title, "$options": "i"}
    news = search_news({"title": title_insensitive})
    print(news)
    list_news = []
    for post in news:
        list_news.append((post["title"], post["url"]))

    return list_news


def search_by_date(date):
    try:

        date_formated = (
            datetime.strptime(date, "%Y-%m-%d")
            .strftime("%d-%m-%Y")
            .replace("-", "/")
        )

        news = search_news({"timestamp": date_formated})

        list_news = []

        for post in news:
            list_news.append((post["title"], post["url"]))

        return list_news
    except ValueError:
        raise ValueError("Data inválida")


def search_by_category(category):
    pass


search_by_title("Algoritmos")
