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
]
