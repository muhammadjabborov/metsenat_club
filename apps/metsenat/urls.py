from django.urls import path
from metsenat import views

urlpatterns = [
    path("sponsor/create/", views.CreateSponsorView.as_view(), name="create_sponsor"),
    path("sponsors/", views.ListSponsorsView.as_view(), name="sponsors"),
    path('sponsor/<int:id>/', views.DetailSponsorView.as_view(), name="detail_sponsor"),
    path('sponsor/update/<int:id>/', views.UpdateSponsorView.as_view(), name="update_sponsor"),
    path("university/create/", views.CreateUniversityView.as_view(), name="create_university"),
    path("student/create/", views.CreateStudentView.as_view(), name="create_student"),
    path("students/", views.ListStudentsView.as_view(), name="students"),
    path('student/<int:id>/', views.DetailStudentView.as_view(), name="detail_student"),
    path('student/update/<int:id>/', views.UpdateStudentView.as_view(), name="update_student"),
    path("student/sponsor/create", views.CreateStudentSponsorView.as_view(), name="create_student_sponsor"),
    path('student/sponsor/update/<int:id>/', views.UpdateStudentSponsorView.as_view(), name="update_student_sponsor"),
    path("dashboard/", views.DashboardData.as_view(), name="dashboard"),
    path("dashboard/students", views.DashboardLineStudent.as_view(), name="dashboard_student"),
    path("dashboard/sponsor", views.DashboardLineSponsor.as_view(), name="dashboard_sponsor"),
]
