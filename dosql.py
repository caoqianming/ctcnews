import sqlite3,random
conn = sqlite3.connect('wxnews.db')
cursor = conn.cursor()
cursor.execute('select count(*) from news')
i = cursor.fetchall()[0][0]
print(i)
x = random.randint(0,i)
cursor.execute('select imgurl from news where id = "'+ str(x) +'"')
print(cursor.fetchall()[0][0])
