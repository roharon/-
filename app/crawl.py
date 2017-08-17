from bs4 import BeautifulSoup
import requests

def Crawl():
    req = requests.get('http://www.mafra.go.kr/list.jsp?id=34366&pageNo=1&NOW_YEAR=2017&group_id=4&menu_id=72&link_menu_id=&division=B&board_kind=C&board_skin_id=C1&parent_code=71&link_url=&depth=2&code=left&link_target_yn=&menu_introduction=&menu_name=%C1%A4%C3%A5%BA%D0%BE%DF%BA%B0%C0%DA%B7%E1&popup_yn=N&reference=1&tab_yn=N')

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    egg_lists = soup.select('td')

    #print(egg_lists)
    data = []

    for eggs in egg_lists:
        data.append(eggs.text)
    data = data[4:]
    #테이블에 보이는 연번부터
    #print(data)

    listing = []
    count = 0
    for i in range(0, 1000):
        try:
            adding = [data[0+11*i], data[1+11*i], data[2+11*i], data[3+11*i], data[4+11*i], data[5+11*i],
                  data[6 + 11 * i], data[7+11*i], data[8+11*i], data[9+11*i], data[10+11*i]]
        except:
            break

        count = i
        listing.append(adding)

    print(listing)

    return [count, listing]


