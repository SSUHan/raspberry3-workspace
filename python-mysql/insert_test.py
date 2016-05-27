
#-*- coding: utf-8 -*-
import MySQLdb as mydb

db = mydb.connect("localhost", "root", "raspberry", "mysql_test")
cur = db.cursor()
cur.execute("insert into student values (4, '건프', now())")

cur.execute("select * from student")

while True:
    student = cur.fetchone()
    if not student:
        break
    print student
cur.close()
db.close()
