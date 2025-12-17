from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.student_logout, name='student_logout'),
    path('marks/', views.student_marks, name='student_marks'),
    path('attendance/', views.student_attendance, name='student_attendance'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('add-student/', views.add_student, name='add_student'),
    path('staff-login/', views.staff_login, name='staff_login'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff-logout/', views.staff_logout, name='staff_logout'),
    path('students/', views.view_student, name='view_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('staff/courses/', views.courses, name='courses'),
    path('staff/add-courses/', views.add_courses, name='add_courses'),
    path('staff/course/<int:course_id>/subjects/', views.course_subjects, name='course_subjects'),
    path('staff/course/<int:course_id>/add-subject/', views.add_subject, name='add_subject'),


 



]
