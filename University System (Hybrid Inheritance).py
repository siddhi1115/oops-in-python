class Person:
    def display_person(self):
        print("I am a Person.")

class Student(Person):
    def display_student(self):
        print("I am a Student.")

class Teacher(Person):
    def display_teacher(self):
        print("I am a Teacher.")

class TeachingAssistant(Student, Teacher):
    def display_ta(self):
        print("I am a Teaching Assistant (TA).")

ta = TeachingAssistant()

ta.display_person()
ta.display_student()
ta.display_teacher()
ta.display_ta()