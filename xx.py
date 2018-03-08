import sqlite3
conn = sqlite3.connect('wxnews.db')
cursor = conn.cursor()
#cursor.execute('select * from news where wxhref in (select wxhref from news group by wxhref having count(wxhref) > 1')
#cursor.execute('select count(*) from news where wxhref =  '+ '"http://mp.weixin.qq.com/s?__biz=MjM5Mjg5NzQwMQ==&mid=2650347768&idx=1&sn=eee70e8a392f4212420a72d95a7a87c1&scene=0"')
#cursor.execute('select count(*) from news where ispublished = "1"')
#if cursor.fetchall()[0][0] == 0:
#    cursor.execute('update news set ispublished ="1" where ispublished = "5"')
wxhref = '123'
cursor.execute('select count(*) from news where wxhref = "%s"'% wxhref)
print(cursor.fetchall()[0][0])
conn.commit()
cursor.close()
conn.close()

