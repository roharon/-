import sqlite3

def db_to_views():
    con = sqlite3.connect('./DB/egg_list.db')
    cur = con.cursor()

    listing = ['연번', '시도', '농가명', '주소', '인증사항', '검사기관', '시료 채취일', '검출농약', '검출양(mg/kg)', '기준', '난각코드']
    cur.execute('SELECT 난각코드 from Egg')

    egg_list = cur.fetchall()

    return egg_list