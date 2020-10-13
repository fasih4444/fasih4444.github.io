from django.urls import path
from .views import (
    home,
    student_portal, 
    teacher_portal,
    student_marksheet,
    marksheet_pdf, 
    profile, 
    student_info,
    MarksheetUpdateView,
    admin_portal,
    students_admin,
    TeachersAdminView,
    student_detail_admin,
    TeacherDetailAdminView,
    create_user,
    create_profile,
    create_student,
    classes_view,
    class_detail_view,
    edit_class_teachers,
    finish_session,
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('student-portal/', student_portal, name='student-portal'),
    path('marksheet/<str:username>/<int:grade>/', student_marksheet, name='student-marksheet'),
    path('marksheet/<str:username>/<int:grade>/pdf/', marksheet_pdf, name='marksheet-pdf'),
    path('teacher-portal/', teacher_portal, name='teacher-portal'),
    path('student/<str:username>/', student_info, name='student-info'),
    path('teacher-portal/marksheet/<int:pk>/update/', MarksheetUpdateView.as_view(), name='update-marksheet'),
    path('admin-portal/', admin_portal, name='admin-portal'),
    path('admin-portal/students/', students_admin, name='students-admin'),
    path('admin-portal/student/<str:username>/', student_detail_admin, name='student-detail-admin'),
    path('admin-portal/teachers/', TeachersAdminView.as_view(), name='teachers-admin'),
    path('admin-portal/teacher/<int:pk>/', TeacherDetailAdminView.as_view(), name='teacher-detail-admin'),
    path('admin-portal/create-user/', create_user, name='create-user'),
    path('admin-portal/create-profile/<str:username>/', create_profile, name='create-profile'),
    path('admin-portal/add-student-info/<str:username>/', create_student, name='create-student'),
    path('admin-portal/classes/', classes_view, name='classes'),
    path('admin-portal/classes/<int:grade>/', class_detail_view, name='class-detail'),
    path('admin-portal/classes/<int:grade>/edit/', edit_class_teachers, name='edit-class-teachers'),
    path('admin-portal/finish-session/', finish_session, name='finish-session'),
]