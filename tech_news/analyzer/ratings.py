from tech_news.database import search_news


def top_5_categories():
    all_news = search_news(None)

    count = {}

    for news in all_news:
        category = news["category"]

        if category in count:
            count[category] += 1
        else:
            count[category] = 1

    sort = sorted(count, key=lambda x: count[x], reverse=True)[:5]
    return sort
