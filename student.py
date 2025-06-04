from data import connection


def student_menu(roll_no):
    while True:
        print("""\nStudent MEnu:
1.view details
2.view marks
3.view timetable
logout""")
        choice=input("enter choice:")

        if choice=='1':
            view_details(roll_no)
        elif choice=='2':
            view_marks(roll_no)
        elif choice=='3':
            view_timetable(roll_no)
        elif choice=='4':
            print("logging out...")
            break
        else:
            print("invalid choice.")
def view_details(roll):
    con=connection()
    cur=con.cursor()
    cur.execute("select * from students where roll_no=%s",(roll,))
    print("student details:")
    print(cur.fetchone())
    con.close()
def view_marks(roll):
        con = connection()
        cur = con.cursor()
        cur.execute("select subject, marks FROM WHERE roll_no = %s", (roll,))
        print("Student marks:")
        for row in cur.fecthall():
             print(row)
        con.close()
student_menu(23)