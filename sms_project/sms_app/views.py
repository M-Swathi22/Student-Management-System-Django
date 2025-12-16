from django.shortcuts import render, redirect
from .models import Student

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