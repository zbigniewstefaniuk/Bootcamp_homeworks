from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    PESEL_no = Column(Integer(15))
    phone = Column(Integer(10))
    address = Column(String(50))

    def __repr__(self):
        return f"Student({self.first_name}, {self.last_name}, {self.PESEL_no}, {self.phone}, {self.address})"


class StudentGrade(Base):
    __tablename__ = 'students_grades'
    enrollemnt_id = Column(Integer(20))
    course_id = Column(Integer(15))
    student_id = Column(Integer(10))
    grade = Column(String(10))

    def __repr__(self):
        return f"Student Grade({self.enrollemnt_id},{self.course_id}, {self.student_id}, {self.grade})"


class Course(Base):
    __tablename__ = 'courses'
    title = Column(String(30))
    students_credits = Column(String(30))
    course_id = Column(Integer(15))
    department_id = Column(Integer(20))
    start_date = Column(Integer(10))
    end_date = Column(Integer(10))
    price = Column(Integer(20))

    def __repr__(self):
        return f"Courses({self.title},{self.course_id}, {self.start_date}, {self.end_date},{self.department_id}," \
               f"{self.students_credits}, {self.price})"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
tony = Student(first_name='Tony', last_name='Tony Stark',
               PESEL_no='12121255555')
session.add(tony)
session.query(Student).all()
