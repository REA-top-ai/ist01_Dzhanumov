from client.api_methods import get_top_headlines
import pprint
from parsing_filter.filter import filter_news
#нес тоит тут хранить ключ
API_KEY = "72e31e2f8c6441f39612cf044be24ba6"

if __name__ == '__main__':

    return_list = []
    page = 1

    while len(return_list) < 50:

        result = get_top_headlines(API_KEY, q='new', pageSize=50, page=page)
        filtered = filter_news(result)
        return_list.extend(filtered)
        page += 1

    return_list = return_list[:50]

    pprint.pprint(return_list)
    print(len(return_list))
