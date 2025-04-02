from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth

import json

from time import sleep

def fetch(ts,url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    # get meta data from url
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    data_str = soup.find('script', id="__NEXT_DATA__").text

    # extract data
    data = json.loads(data_str)
    question = data['props']['pageProps']['dehydratedState']['queries'][1]['state']['data']['question']
    q_number = question['questionFrontendId'].zfill(4)
    q_title = question['title']
    q_slug = question['titleSlug']
    q_lvl = question['difficulty']
    q_content = question['content']
    q_topics = [tag['slug'] for tag in question['topicTags']]

    # write sample-data.json
    # with open("sample-data.json", "w", encoding="utf-8") as file:
    #     file.write(json.dumps(question))
    
    # create new dir
    # write .md file
    with open(f"./{q_number}-README.md", "w", encoding="utf-8") as file:
        file.write(f'# [{q_number}. {q_title}]({url})\n\n')
        file.write(f'\n> {q_lvl}\n\n')
        for tag in q_topics:
            file.write(f'- {tag}\n')
        file.write('\n\n\n')
        file.write('## Question\n\n\n')
        file.write(q_content)
        file.write('\n\n\n## Solution\n\n')
        file.write('- time  : O()\n')
        file.write('- space : O()\n')
    with open(f"./{q_number}-solution.py", "w", encoding="utf-8") as file:
        file.write('from typing import List\n\n')
        file.write('# Time : Beats 0000 %\n# Memo : Beats 0000 %\n')
    print(f'create : {q_number}')
    
    # write .csv log
    with open("./leetcode-log-helper.csv", 'a', encoding="utf-8") as log:
        log.write(f'{ts}, {q_number}, {q_slug}, {q_lvl}, "{q_topics}"\n')
    print('logged')


if __name__ == '__main__':
    data = [
        ['2024-01-04T11:49:00','https://leetcode.com/problems/container-with-most-water'],
        ['2024-01-04T13:32:00','https://leetcode.com/problems/3sum'],
        ['2024-01-04T14:40:00','https://leetcode.com/problems/remove-nth-node-from-end-of-list'],
    ]
    for ts,url in data:
        fetch(ts,url)
        sleep(1)