import requests
import pprint
from client.api_methods import get_top_headlines
from parsing_filter.filter import filter_news
from config import NEWS_API_KEY, MISTRAL_API_KEY


def generate_annotation(news_list):
    url = "https://api.mistral.ai/v1/chat/completions"

    prompt = f"""
Ты — аналитик новостей.

На основе списка новостей за последний день сделай аналитическую сводку
на русском языке объемом 250-300 слов.

Требования:
- не перечисляй новости по отдельности
- выдели ключевые события
- объясни их значение
- сделай общий вывод

Новости:
{news_list}
"""

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-small",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Ошибка API: {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]


def save_to_file(text):
    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == '__main__':

    return_list = []
    page = 1

    while len(return_list) < 50:
        result = get_top_headlines(NEWS_API_KEY, q='technology', pageSize=50, page=page)
        filtered = filter_news(result)
        return_list.extend(filtered)
        page += 1

    return_list = return_list[:50]

    return_list = [
        {
            "title": n.get("title"),
            "description": n.get("description")
        }
        for n in return_list
    ]

    pprint.pprint(return_list)
    print(len(return_list))

    summary = generate_annotation(return_list)

    print(summary)

    save_to_file(summary)
