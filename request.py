import requests
import bs4Code

# with open('data.json', 'r', encoding='utf-8') as file:
#     headers = json.loads(file.read())

def find_data(query)->list:
    
    headers = {
        "authority": "tashkent.hh.uz",
        "method": "GET",
        "path": f"/search/vacancy?text={query}&salary=&ored_clusters=true&area=2778&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "uz-UZ,uz;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie": "__ddg1_=TInMBLtcdtq73pnBiDOi; redirect_host=tashkent.hh.uz; hhuid=SKWmXENx9B1RzGijDfc3eA--; region_clarified=NOT_SET; ...",
        "priority": "u=0, i",
        "referer": "https://tashkent.hh.uz/search/vacancy?text=python&area=2778&hhtmFrom=main&hhtmFromLabel=vacancy_search_line",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }
    url = f'https://tashkent.hh.uz/search/vacancy?text={query}&salary=&ored_clusters=true&area=2778&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line'
    session = requests.Session()
    respons = session.get(url, headers=headers)
    if respons.status_code == 200:
        result = bs4Code.format_data(respons.text, session)
        return result
        
    return []

if __name__ == "__main__":
    # Example usage
    result = find_data('php')
    print(result)