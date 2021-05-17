import requests
from bs4 import BeautifulSoup as bs

def crawling():
    url = 'https://www.passport.go.kr/new/board/passport.php'
    html = requests.get(url).text

    soup_obj = bs(html, "html.parser")
    nums = soup_obj.select('#content > table > tbody > tr > td.subject')
    
    return len(nums)