from tech_news.database import search_news


def search_by_title(title):
    title_insensitive = {"$regex": title, "$options": "i"}
    news = search_news({"title": title_insensitive})
    list_news = []

    for post in news:
        list_news.append((post["title"], post["url"]))

    return list_news


def search_by_date(date):
    pass


def search_by_category(category):
    pass


search_by_title("Algoritmos")
