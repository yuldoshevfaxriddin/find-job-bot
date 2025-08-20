from bs4 import BeautifulSoup

import re

def format_data(text, session=None):
    with open('data.html', 'w', encoding='utf-8') as file:
        file.write(text)
    soup = BeautifulSoup(text, 'lxml')
    cards = soup.find_all("div", class_=re.compile(r"^vacancy-info"))
    vacansys = []
    for card in cards:
        title = card.find("h2").find("a").text.strip()
        link = card.find("h2").find("a")['href']
        company = re.sub(r"\s+", " ", card.select("a div span span")[1].text).strip()
        location = card.find(attrs={"data-qa": "vacancy-serp__vacancy-address"})
        img = BeautifulSoup(session.get(link).text, 'lxml').find('div',attrs={"data-qa": "vacancy-company-logo"})
        print('img',img)
        vacansys.append({
            "title": title,
            "link": link,
            "company": company,
            "location": location.text.strip() if location else "Not specified",
            # "salary": salary
        })
    return vacansys
