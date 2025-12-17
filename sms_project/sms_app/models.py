from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    register_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.register_number} - {self.name}"



class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('Present','Present'),('Absent','Absent')))

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.status}"