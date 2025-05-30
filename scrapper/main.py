import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth

import json
from pathlib import Path

import datetime

def main():
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

    # get url from CLI
    url = sys.argv[1]

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
    new_dir = f'./{q_number}_{q_slug}'
    Path(new_dir).mkdir(parents=True, exist_ok=True)

    
    # write .md file
    with open(f"{new_dir}/README.md", "w", encoding="utf-8") as file:
        file.write(f'# [{q_number}. {q_title}]({url})\n\n')
        file.write(f'\n> {q_lvl}\n\n')
        for tag in q_topics:
            file.write(f'- {tag}\n')
        file.write('\n\n\n')
        file.write('## Question\n\n\n')
        file.write(q_content)
        file.write('\n\n\n## Solution\n\n')
        file.write('- time  : $O()$\n')
        file.write('- space : $O()$\n\n---\n')
    with open(f"{new_dir}/solution.py", "w", encoding="utf-8") as file:
        file.write('from typing import List\n\n')
        file.write('# Time : Beats 0000 %\n# Memo : Beats 0000 %\n')
    print(f'create : {new_dir}')
    
    # write .csv log
    with open("./leetcode-log.csv", 'a', encoding="utf-8") as log:
        timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        log.write(f'{timestamp}, {q_number}, {q_slug}, {q_lvl}, "{q_topics}", "[]"\n')
    print(f'logged')


if __name__ == '__main__':
    main()