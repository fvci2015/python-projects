import pymysql
db=pymysql.connect(host='localhost',user='root',password='',database='attendance_tracker')
cursor=db.cursor()
SQL="CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL, UNIQUE KEY name_unique(name))"
cursor.execute(SQL)
db.commit()
db.close()