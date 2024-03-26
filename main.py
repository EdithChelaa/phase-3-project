from sqlalchemy.orm import sessionmaker
from models.models import Student, Teacher, Subject, Enrollment, Base, engine

# Create database tables if they don't exist
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Teacher is added to the system
def register_teacher():
    print("Teacher Registration")
    name = input("Enter teacher's name: ")
    teacher = Teacher(teacher_name=name)
    session.add(teacher)
    session.commit()
    print(f"Registered teacher: {name}")

# Teacher adds subject
def add_subject():
    print("Add Subject")
    name = input("Enter subject name: ")
    teacher_id = int(input("Enter eacher ID: "))
    subject = Subject(sub_name = name, teacher_id = teacher_id)
    session.add(subject)
    session.commit()
    print(f"Added subject: {name}")

# Teacher to add the student
def add_student():
    print("Add Student")
    name = input("Enter student's name: ")
    adm = input("Enter admission number: ")
    student = Student(student_name=name, student_adm=adm)
    session.add(student)

    session.commit()
    print(f"Added student: {name}, Admission Number: {adm}")

# Teacher enrolls student to a subject
def enroll_student():
    print("Enroll Student to Subject")
    student_id = int(input("Enter student ID: "))
    sub_id = int(input("Enter subject ID: "))
    student = session.query(Student).filter_by(student_id=student_id).first()
    subject = session.query(Subject).filter_by(sub_id=sub_id).first()
    if not student or not subject:
        print("Student or course not found.")
        return
    
    enrollment = Enrollment(student_id=student_id, sub_id=sub_id)
    session.add(enrollment)
    session.commit()
    print(f"Student {student.student_name} enrolled in subject {subject.sub_name}")

# Teacher to add the student marks
def add_marks():
    print("Add Marks")
    student_id = int(input("Enter student ID: "))
    student = session.query(Student).filter_by(student_id=student_id).first()
    
    if not student:
        print("Student not found.")
        return

    marks = int(input("Enter academic marks: "))
    student.student_marks = marks
    session.commit()
    print(f"Marks added for {student.student_name}: {marks}")

# Teacher views all the student marks
def view_makrs():
    print("Students and their Marks")
    students = session.query(Student).all()
    if not students:
        print("Students not found.")
        return
    for student in students:
        print(f"Student Name: {student.student_name}, Marks: {student.student_marks}")

def main():
    while True:
        print("\n Class Merit Management System")
        print("1. Register Teacher")
        print("2. Tacher adds subject")
        print("3. Teacher adds Student")
        print("4. Teacher enrolls student to subject")
        print("5. Teacher adds Student Marks")
        print("6. Teacher views all student marks")
        print("7. Exit")
        option = input("Enter Your Option: ")

        if option == "1":
            register_teacher()
        elif option == "2":
            add_subject()
        elif option == "3":
            add_student()
        elif option == "4":
            enroll_student()
        elif option == "5":
            add_marks()
        elif option == "6":
            view_makrs()
        elif option == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()