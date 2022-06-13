import sqlite3

k = 10000   #время в секундах, в течение которого от последней записи мы хотим получить

num = 0

tn = sqlite3.connect("History")

u = tn.cursor()
g = tn.cursor()
i = tn.cursor()

u.execute("SELECT last_visit_time FROM urls ORDER BY -last_visit_time LIMIT 1")

ftime = u.fetchall()

for n in g.execute("SELECT last_visit_time FROM urls ORDER BY -last_visit_time"):
    #print(n)
    num = num + 1
    if n[0] < ftime[0][0] - 10000*1000000:
        break


i.execute("SELECT url FROM urls ORDER BY -last_visit_time LIMIT :lim", {"lim": num})

k = i.fetchall()

print(k)
