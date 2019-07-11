from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def crawling_Context(page_url):
    # print('page_url: ', page_url)

    html_innerContext = urlopen(page_url)
    htmlObject_context = BeautifulSoup(html_innerContext, "html.parser")

    # print(htmlObject_context.find('div', attrs={'class', 'pr-info'}).text)
    post_date = htmlObject_context.find('span', attrs={'class', 'date-display-single'}).text
    # post_title = htmlObject_context.find('h1', attrs={'id', 'node-title'}).text
    post_title = htmlObject_context.select('h1#node-title')[0].text.strip()
    post_content = htmlObject_context.find('div', attrs={'class', 'field field--name-field-pr-body field--type-text-long field--label-hidden'}).text

    # print(post_title)
    # parsing post_content

    post_content_List = post_content.split('\n')
    post_content_List2 = []
    for d in range(len(post_content_List)):
        post_content_List2.append(''.join(post_content_List[d].split(',')))

    print(post_content_List2)

    for a in range(len(post_content_List)):

        # remove elements of list which have words as below.
        filtering_list = [' is ', ' are ', ' am ', ' was ', ' were ', ' been ', ' though ', ' although ', ' even though ', ' while ', ' if ',
                           ' only if ', ' unless ', ' until ', ' provided that ', ' assuming that ', ' even if ', ' in case ',
                           ' in case that ', ' lest ', ' than ', ' rather than ', ' whether ', ' as much as ', ' whereas ', ' after ',
                           ' as long as ', ' as soon as ', ' before ', ' by the time ', ' now that ', ' once ', ' since ', ' till ',
                           ' until ', ' when ', ' whenever ', ' while ', ' because ', ' and ', ' since ', ' so that ', ' in order ',
                           ' in order that ', ' why ', ' that ', ' what ', ' whatever ', ' which ', ' whichever ', ' who ', ' whoever ',
                           ' whom ', ' whomever ','however', ' whose ', ' how ', ' as though ', ' as if ', ' where ', ' wherever ', ' about ',
                           ' above ', ' across ', ' after ', ' against ', ' along ', ' among ', ' around ', ' because of ', ' before ',
                           ' behind ', ' below ', ' beneath ', ' beside ', ' between ', ' close to ', ' down ', ' during ', ' except ',
                           ' inside ', ' instead of ', ' into ', ' like ', ' near ', ' off ', ' on top of ', ' onto ', ' out of ',
                           ' outside ', ' over ', ' past ', ' since ', ' through ', ' toward ', ' under ', ' until ', ' up ', ' upon ',
                           ' within ', ' without ', ' at ', ' by ', ' for ', ' from ', ' in ', ' or ', ' of ', ' on ', ' to ', ' with ', ' me ', ' my ',
                           ' mine ', ' myself ', ' you ', ' you ', ' your ', ' yours ', ' yourself ', ' he ', ' him ', ' his ', ' his ',
                           ' himself ', ' she ', ' her ', ' her ', ' hers ', ' herself ', ' its ', ' itself ', ' our ', ' ours ',
                           ' ourselves ', ' you ', ' you ', ' your ', ' yours ', ' yourselves ', ' they ', ' them ', ' their ', ' theirs '
                           ' themselves ', 'has', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                           'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                           'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                           'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
                           'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
                           'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'District of Columbia',
                           'American Samoa', 'Guam', 'Northern Mariana Islands', 'Puerto Rico', 'U.S. Virgin Islands', 'DC', 'media',
                           'researchers', 'victims', 'advocacy groups','Facebook', 'Skype', 'instagram', 'Linkedin', 'twitter', 'QQ', 'Weibo', 'Google',
                           'criminal', 'fine', 'temporary', 'tattoos', 'forensic', 'interviews', 'penalty', 'addition'
                          ]

        for c in range(len(filtering_list)):
            if filtering_list[c].upper() in post_content_List[a].upper():
                post_content_List[a] = 'NULL'

        post_content_List[a] = re.sub('[-=.#/?:$}"”“[\]()0-9\xa0§]', '', post_content_List[a].replace("'s", "").replace("' s", "").replace("’s", "").strip())
    post_content_List = [e for e in post_content_List if e not in ('NULL', '')]


    print(post_content_List)
    resultContext_only_Name = ''

    return resultContext_only_Name