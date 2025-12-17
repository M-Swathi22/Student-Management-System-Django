from django.shortcuts import render, redirect
from .models import Student

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
    return redirect('student_login')

from django.shortcuts import render, redirect
from .models import Student, Marks, Attendance

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
