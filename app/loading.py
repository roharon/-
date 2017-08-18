import sqlite3

def loading_list(request):

    con = sqlite3.connect('./DB/egg_list.db')
    cur = con.cursor()

    try:
        cur.execute('SELECT 난각코드 from Egg')
    except:
        pass

    info = cur.fetchall()
    print(info)
    egg_list = []

    for i in range(0, len(info)):
        egg_list.append(info[i][0])


    print(egg_list)
    con.close()

    return egg_list

#loading_list('aa')