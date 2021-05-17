import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

def crawling():
    url = 'https://www.passport.go.kr/new/board/passport.php'
    response = requests.get(url)

    if response.status_code == 200:
        html = requests.get(url).text
        soup_obj = bs(html, "html.parser")
        nums = soup_obj.select('#content > table > tbody > tr > td.subject')
        n = len(nums)
        if n == 3:
            utc0 = datetime.now()
            utc9 = utc0 - timedelta(hours=-9)
            utc9_str = utc9.strftime("%Y-%m-%d %H:%M:%S")
        
            msg = '현재(UTC+09) ' + utc9_str + '\n' + '  현재 게시물이 3개 입니다.'
            return msg
        if n > 3:
            msg = '게시물이 4개 이상입니다. \n' + url
            return msg
        if not n :
            msg = '크롤링이 제대로 되고 있지 않는듯.. 확인바람.'
            return msg

    else :
        return response.status_code