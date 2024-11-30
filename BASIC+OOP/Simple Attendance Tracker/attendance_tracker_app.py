import pymysql

class AttendanceTracker:
    
    #creating default constructor
    def __init__(self):
        self.db=pymysql.connect(host='localhost',user='root',password='',database='attendance_tracker')
        self.cursor=self.db.cursor()

    #insert student into the database
    def insertNewStudent(self,student_name):
        try:
            self.cursor.execute("INSERT INTO students(name) VALUES(%s)",(student_name,))
            self.db.commit()
            insert_result=self.cursor.rowcount()
            if insert_result>0:
                print("DATA OF STUDENT INSERTED SUCCESSFULLY")
                print("\n")
                print("\n")
        except Exception as e:
            print(str(e))

    def MarkAttendance(self,student_name):
        #check if the student exists
        try:
            self.cursor.execute("SELECT * from students WHERE name=%s",(student_name,))
            self.db.commit()
            student=self.cursor.fetchone()

            #if student does not exist return an error
            if not student:
                print("This student does not exist")
                return

            #mark attendance for student
            self.cursor.execute("INSERT INTO attendance(student_id,attendance_date) VALUES(%s,CURDATE())",(student[0]))
            self.db.commit()
            print("ATTENDANCE MARKED SUCCESFULLY FOR STUDENT NAME: ",student_name)
        except Exception as e:
            print(str(e))
    
    def displayStudentAttendance(self,student_name):
        try:
            self.cursor.execute("SELECT * from students WHERE name=%s",(student_name,))
            self.db.commit()
            student=self.cursor.fetchone()

            if not student:
                print("Student name does not exist")
                return

            self.cursor.execute("SELECT attendance_date from attendance WHERE student_id=%s",(student[0],))
            self.db.commit()
            attendance=self.cursor.fetchall()

            if not attendance:
                print("No attendance records found")
                return

            print("Dates Present: \n")
            for row in attendance:
                print(row)
        except Exception as e:
            print(str(e))
            return
    def displayAllAttendance(self):
        try:
            self.cursor.execute("SELECT s.id,s.name,a.attendance_date FROM students s LEFT JOIN attendance a ON a.student_id=s.id")
            self.db.commit()
            result=self.cursor.fetchall()

            if not result:
                print("No DATA FOUND")
                return 
            
            print("RECORDS: \n")
            for row in result:
                print(row)
        except Exception as e:
            print("Error: ",str(e))

def main():
    At=AttendanceTracker()
    while True:
        print("1. Insert new student\n2. Mark Attendance.\n3. View a students attendance.\n4.Display attendance of all student")
        choice=int(input("Enter your choice: "))
        if choice==1:
            student_name=input("Enter the name of the student: ")
            At.insertNewStudent(student_name)
        elif choice==2:
            student_name=input("Enter the name of the student: ")
            At.MarkAttendance(student_name)
        elif choice==3:
            student_name=input("Enter the name of the student: ")
            At.displayStudentAttendance(student_name)
        elif choice==4:
            At.displayAllAttendance()
        elif choice==5:
            print("Exiting the program\n\n\n")
            exit(0)
        else:
            print("Please enter a valid input")

if __name__=="__main__":
    main()