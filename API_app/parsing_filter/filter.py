import string


def filter_news(news: dict):
    if not news or "articles" not in news:
        return []

    articles = news.get("articles", [])
    result = []

    for article in articles:
        if not article:
            continue

        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        if (
            title and title.strip() and
            url and
            description and len(description) >= 50
        ):
            filtered_article = {
                "title": title,
                "source": article.get("source", {}).get("name"),
                "published": article.get("publishedAt"),
                "author": article.get("author")
            }

            result.append(filtered_article)

    return result