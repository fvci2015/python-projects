import pymysql
db=pymysql.connect(host='localhost',user='root',password='',database='attendance_tracker')
cursor=db.cursor()
SQL="CREATE TABLE attendance(id INT AUTO_INCREMENT PRIMARY KEY,student_id INT REFERENCES students(id),attendance_date DATE)"
cursor.execute(SQL)
db.commit()
db.close()  