from tech_news.database import db


def top_5_categories():
    all_news = list(db.news.find({}, {"_id": False, "category": True}))

    count = {}

    for news in all_news:
        category = news["category"]

        if category in count:
            count[category] += 1
        else:
            count[category] = 1

    sort = sorted(count, key=lambda x: (count[x], x), reverse=False)[:5]
    return sort
