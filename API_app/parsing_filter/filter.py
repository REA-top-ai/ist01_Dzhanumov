import string

def filter_news(news: dict):
    chars_for_filter = (
    [chr(i) for i in range(ord('а'), ord('я') + 1)] + ['ё'] +
    [chr(i) for i in range(ord('А'), ord('Я') + 1)] + ['Ё'] +
    list(string.ascii_lowercase) +
    list(string.ascii_uppercase) +
    list(string.digits) +
    list(string.punctuation)

    ) #все возможные символы, кроме пробела
    only_arti = news['articles']
    result = []
    for new in only_arti:  
        articles = news['articles']
    result = []

    for article in articles:
    #в словарях лучше действовать через функцию  get
        if (
            article['title'] and article['title'].strip() and
            article['url'] and
            article['description'] and len(article['description']) >= 50
        ):

            filtered_article = {
                "title": article["title"],
                "source": article["source"]["name"],
                "published": article["publishedAt"],
                "author": article["author"]
            }

            result.append(filtered_article)

    return result

