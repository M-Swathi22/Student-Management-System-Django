from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Staff, Marks, Attendance, Subject
from django.utils import timezone


def home(request):
    return render(request, 'home.html')


def student_login(request):
    if request.method == "POST":
        reg_no = request.POST['register_number']
        dob = request.POST['dob']

        try:
            student = Student.objects.get(register_number=reg_no, dob=dob)
            request.session['student_id'] = student.id
            return redirect('student_dashboard')
        except Student.DoesNotExist:
            return render(request, 'student_login.html', {'error': 'Invalid Register Number or Date of Birth'})

    return render(request, 'student_login.html')

def student_dashboard(request):
    if not request.session.get('student_id'):
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])
    return render(request, 'student_dashboard.html', {'student': student})


def student_logout(request):
    request.session.flush()
    return redirect('home')

def student_marks(request):
    if not request.session.get('student_id'):
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])
    marks = Marks.objects.filter(student=student)  # ✅ Correct

    return render(request, 'student_marks.html', {'marks': marks})

def student_attendance(request):
    if not request.session.get('student_id'):
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])
    attendance = Attendance.objects.filter(student=student)  # ✅ Correct

    return render(request, 'student_attendance.html', {'attendance': attendance})

def staff_login(request):
    return render(request, 'staff_login.html')

def add_student(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            register_number=request.POST['register_number'],
            dob=request.POST['dob'],
            age=request.POST['age'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            course_id=request.POST['course']
        )
        return redirect('add_student')

    return render(request, 'add_student.html', {'courses': courses})

def staff_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            staff = Staff.objects.get(email=email, password=password)
            request.session['staff_id'] = staff.id
            return redirect('staff_dashboard')
        except Staff.DoesNotExist:
            return render(request, 'staff_login.html', {'error': 'Invalid Email or Password'})

    return render(request, 'staff_login.html')

def staff_dashboard(request):
    if not request.session.get('staff_id'):
        return redirect('staff_login')

    staff = Staff.objects.get(id=request.session['staff_id'])
    return render(request, 'staff_dashboard.html', {'staff': staff})

def staff_logout(request):
    request.session.flush()
    return redirect('home')


def view_student(request):
    students = Student.objects.all().order_by('register_number')
    return render(request, 'view_student.html', {'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()

    if request.method == 'POST':
        student.name = request.POST['name']
        student.register_number = request.POST['register_number']
        student.dob = request.POST['dob']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.address = request.POST['address']
        student.course_id = request.POST['course']
        student.save()
        return redirect('view_students')

    return render(request, 'edit_student.html', {'student': student, 'courses': courses})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('view_students')

def add_marks(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST['student']
        subject_id = request.POST['subject']
        marks_obtained = request.POST['marks_obtained']
        total_marks = request.POST['total_marks']

        # Check if marks already exist for student-subject
        existing = Marks.objects.filter(student_id=student_id, subject_id=subject_id).first()
        if existing:
            existing.marks_obtained = marks_obtained
            existing.total_marks = total_marks
            existing.save()
        else:
            Marks.objects.create(
                student_id=student_id,
                subject_id=subject_id,
                marks_obtained=marks_obtained,
                total_marks=total_marks
            )
        return redirect('add_marks')  # Refresh page after submission

    return render(request, 'add_marks.html', {'students': students, 'subjects': subjects})

def add_attendance(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST['student']
        subject_id = request.POST['subject']
        date = request.POST['date']
        status = request.POST['status']  # Present / Absent

        # Check if attendance already exists for student-subject-date
        existing = Attendance.objects.filter(student_id=student_id, subject_id=subject_id, date=date).first()
        if existing:
            existing.status = status
            existing.save()
        else:
            Attendance.objects.create(
                student_id=student_id,
                subject_id=subject_id,
                date=date,
                status=status
            )
        return redirect('add_attendance')  # Refresh page after submission

    today = timezone.now().date()
    return render(request, 'add_attendance.html', {
        'students': students,
        'subjects': subjects,
        'today': today
    })


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def add_courses(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Course.objects.create(name=name)
        return redirect('courses')
    return render(request, 'add_courses.html')

def course_subjects(request, course_id):
    course = Course.objects.get(id=course_id)
    subjects = Subject.objects.filter(course=course)
    return render(request, 'course_subjects.html', {
        'course': course,
        'subjects': subjects
    })


def add_subject(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        name = request.POST['name']
        Subject.objects.create(course=course, name=name)
        return redirect('course_subjects', course_id=course.id)

    return render(request, 'add_subject.html', {'course': course})