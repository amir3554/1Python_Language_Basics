class MySchool:
    def __init__(self, id, name, theme, address,surve ):#المقصود ب ثيم هو اذا كانت مدرسة خاصة \ حكومية \ اساسية ... \علمية الخ...ا
        self.id = id
        self.name = name
        self.theme = theme
        self.address = address
        self.surve = surve

    def surving(self):
        if self.surve:
            return f'The School ({self.name}, {self.address}), is opened at the moment.'
        else:
            return f'The School ({self.name}, {self.address}), is closed at the moment.'
        
    def school_info(self):
        def is_open():
            if self.surve:
                print(f"the School ({self.name}) is surving ")
            else:
                print(f"the School ({self.name}) is not surving ")

        return f'Id : {self.id}, The name of the school is {self.name},Theme is : {self.theme}, Address :{self.address},{is_open()}.'


class WorkerPerson():
    def __init__(self, id, name, age, carreer, notes=''):
        self.id = id
        self.name = name
        self.age = age
        self.carreer = carreer
        self.notes = notes 
        

class Teacher(WorkerPerson):
    def __init__(self, id, name, age, carreer, notes=''):
        super().__init__(id, name, age, carreer, notes)


class Student(WorkerPerson):
    def __init__(self, id, name, age, carreer, notes=''):
        super().__init__(id, name, age, carreer, notes)

'''def teaching(self):
        print(f"the Teacher {self.teachers}, is teaching.")
        return True

    def attendance(self, Is_true):
        if Is_true == True:
            print(f"The {self.students} is attending classes now")
            return True
        else:
            print(f"it seems like {self.students} is absent")
            return False'''  
    


class School:
    def __init__(self, name, address):
        self.name = name  # اسم المدرسة
        self.address = address  # عنوان المدرسة
        self.students = []  # قائمة الطلاب
        self.teachers = []  # قائمة المدرسين

    # وظيفة لإضافة طالب
    def add_student(self, student_name, grade):
        student = {"name": student_name, "grade": grade}
        self.students.append(student)
        print(f"Student {student_name} added to the school.")

    # وظيفة لإضافة مدرس
    def add_teacher(self, teacher_name, subject):
        teacher = {"name": teacher_name, "subject": subject}
        self.teachers.append(teacher)
        print(f"Teacher {teacher_name} added to the school.")

    # وظيفة لعرض قائمة الطلاب
    def list_students(self):
        if not self.students:
            print("No students in the school.")
        else:
            print("Students in the school:")
            for student in self.students:
                print(f"- {student['name']}, Grade: {student['grade']}")

    # وظيفة لعرض قائمة المدرسين
    def list_teachers(self):
        if not self.teachers:
            print("No teachers in the school.")
        else:
            print("Teachers in the school:")
            for teacher in self.teachers:
                print(f"- {teacher['name']}, Subject: {teacher['subject']}")

    # وظيفة لإزالة طالب
    def remove_student(self, student_name):
        for student in self.students:
            if student["name"] == student_name:
                self.students.remove(student)
                print(f"Student {student_name} removed from the school.")
                return
        print(f"Student {student_name} not found.")

    # وظيفة لإزالة مدرس
    def remove_teacher(self, teacher_name):
        for teacher in self.teachers:
            if teacher["name"] == teacher_name:
                self.teachers.remove(teacher)
                print(f"Teacher {teacher_name} removed from the school.")
                return
        print(f"Teacher {teacher_name} not found.")


# إنشاء مدرسة جديدة
my_school = School("Green Valley High", "123 Main St")

# إضافة طلاب
my_school.add_student("Alice", 10)
my_school.add_student("Bob", 11)

# إضافة مدرسين
my_school.add_teacher("Mr. Smith", "Math")
my_school.add_teacher("Ms. Johnson", "English")

# عرض الطلاب والمدرسين
my_school.list_students()
my_school.list_teachers()

'''
# النتائج المتوقعة بعد اضافة الطلاب و المدرسين
Student Alice added to the school.
Student Bob added to the school.
Teacher Mr. Smith added to the school.
Teacher Ms. Johnson added to the school.
Students in the school:
- Alice, Grade: 10
- Bob, Grade: 11
Teachers in the school:
- Mr. Smith, Subject: Math
- Ms. Johnson, Subject: English


# النتائج المتوقعة بعد حذف الطلاب و المدرسين
Student Alice removed from the school.
Teacher Ms. Johnson removed from the school.
Students in the school:
- Bob, Grade: 11
Teachers in the school:
- Mr. Smith, Subject: Math
'''
