from urllib.request import urlopen
from bs4 import BeautifulSoup

from news_crawling_context import crawling_Context

import time
start = time.time()  # 시작 시간 저장

for i in range(0, 3):
    html = urlopen("https://www.justice.gov/news?f%5B0%5D=field_pr_date%3A2019&f%5B1%5D=type%3Apress_release&page=" + str(i))
    htmlObject = BeautifulSoup(html, "html.parser")

    globals()['htmlText'.format(i)] = htmlObject
    print('page number ', str(i + 1))
    titleDIV = htmlObject.find_all('div', attrs={'class': 'views-field views-field-title'})
    news_dict = {}
    for a in range(len(titleDIV)):

        # key: 'page number-newsNumber'
        # value[list1]: news title
        # value[list2]: news url

        value_title = titleDIV[a].find('a').text.strip()
        value_url = 'https://www.justice.gov' + titleDIV[a].find('a')['href']

        news_dict_key = str(i+1) + '-' + str(a+1)
        news_dict_value_list = [value_title, value_url]
        news_dict[news_dict_key] = news_dict_value_list

        crawling_Context(news_dict[news_dict_key][1])
    # print(news_dict)
    print()

    # for b in range(len(titleDIV)):
    #     crawling_Context(news_dict[str(i+1) + '-' + str(b+1)][1])

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
