class Student:
    school = "ABC Public School"

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        return "Fail"

    def display(self):
        print("\nStudent Details")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School:", self.school)


class GraduateStudent(Student):
    def __init__(self, roll_no, name, marks, specialization):
        super().__init__(roll_no, name, marks)
        self.specialization = specialization

    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Grade:", self.grade())


roll_no = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
marks = float(input("Enter Marks: "))
specialization = input("Enter Specialization: ")

student = GraduateStudent(roll_no, name, marks, specialization)
student.display()