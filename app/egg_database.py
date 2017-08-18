import sqlite3
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
            adding = [data[0+14*i], data[1+14*i], data[2+14*i], data[3+14*i], data[4+14*i], data[5+14*i],
                  data[6 + 14 * i], data[7+14*i], data[8+14*i], data[9+14*i], data[10+14*i],
                      data[11+14*i], data[12+14*i], data[13+14*i]]
        except:
            break

        count = i
        listing.append(adding)

    print(listing)
    returning = [count, listing]
    return returning

#사육규모, 비고

def egg_list():

    #con = sqlite3.connect('../DB/egg_list.db')
    con = sqlite3.connect('/home/roharon98/egg/DB/egg_list.db')
    cur = con.cursor()

    try:
        cur.execute("DELETE FROM 연번")
        cur.execute("DELETE FROM 시도")
        cur.execute("DELETE FROM 농가명")
        cur.execute("DELETE FROM 주소")
        cur.execute("DELETE FROM 사육규모")
        cur.execute("DELETE FROM 생산량")
        cur.execute("DELETE FROM 인증사항")
        cur.execute("DELETE FROM 검사기관")
        cur.execute("DELETE FROM 시료채취일")
        cur.execute("DELETE FROM 검출농약")
        cur.execute("DELETE FROM 검출양")
        cur.execute("DELETE FROM 기준")
        cur.execute("DELETE FROM 난각코드")
        cur.execute("DELETE FROM 비고")
    except:
        pass


    listing_size = Crawl()[0]
    listing = Crawl()[1]

    print(listing_size)
    try:
        print('try구문')
        cur.execute("CREATE TABLE Egg(연번 TEXT, 시도 TEXT, 농가명 TEXT, 주소 TEXT, 사육규모 TEXT, 생산량 TEXT, 인증사항 TEXT, 검사기관 TEXT, "
                    "시료채취일 TEXT, 검출농약 TEXT, 검출양 TEXT, 기준 TEXT, 난각코드 TEXT, 비고 TEXT );")
    except:
        pass

    for i in range(1, int(listing_size+1)):
        try:
            value_dict = {'연번': str(listing[i][0]), '시도': str(listing[i][1]),
                          '농가명': str(listing[i][2]),
                          '주소': str(listing[i][3]), '사육규모': str(listing[i][4]), '생산량': str(listing[i][5]),
                          '인증사항': str(listing[i][6]), '검사기관': str(listing[i][7]),
                          '시료채취일': str(listing[i][8]),
                          '검출농약': str(listing[i][9]), '검출양': str(listing[i][10]),
                          '기준': str(listing[i][11]),
                          '난각코드': str(listing[i][12]), '비고': str(listing[i][13]) }
            cur.execute("INSERT INTO Egg(연번, 시도, 농가명, 주소, 사육규모, 생산량, 인증사항, 검사기관, "
                        "시료채취일, 검출농약, 검출양, 기준 , 난각코드, 비고) VALUES (:연번, :시도, :농가명, :주소, :사육규모, :생산량, :인증사항, :검사기관, :시료채취일, :검출농약, :검출양, :기준, :난각코드, :비고);",
                        value_dict)
        except:

            print(i)
            break

    con.commit()
    con.close()


egg_list()