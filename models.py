# track info on books
from sqlalchemy import Column, Integer, String, create_engine,Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

engine = create_engine("sqlite:///schoolmanager.db")

class Student(Base):
    __tablename__ = 'students'

    # Define columns for student information.
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_adm = Column(String)
    student_marks = Column(Integer)
       
    # Define relationships with other tables.

    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))

    teacher = relationship('Teacher', back_populates='students')
    
    enrollments = relationship('Enrollment', back_populates='student')
    subjects = relationship('Subject', secondary='enrollments', back_populates='students')

# Define the Teacher class for the 'teachers' table.
class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String)
    students = relationship('Student', back_populates='teacher')
    subjects = relationship('Subject', back_populates='teacher')
   

# Define the Course class for the 'courses' table.
class Subject(Base):
    __tablename__ = 'subjects'

    # Define columns for course information.
    sub_id = Column(Integer, primary_key=True)
    sub_name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))

    # Define relationships with other tables.
    teacher = relationship('Teacher', back_populates='subjects')
    students = relationship('Student', secondary='enrollments')
    enrollments = relationship('Enrollment', back_populates='subject')

# Define the Enrollment class for the 'enrollments' table.
class Enrollment(Base):
    __tablename__ = 'enrollments'

    # Define columns for enrollment information.
    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    sub_id = Column(Integer, ForeignKey('subjects.sub_id'))

    # Define relationships with other tables.
    student = relationship('Student', back_populates='enrollments')
    subject = relationship('Subject', back_populates='enrollments')


    

Base.metadata.create_all(engine)

