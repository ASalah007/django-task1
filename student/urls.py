from django.urls import path

from student.views import StudentListView, StudentEditView

urlpatterns = [
    path('', StudentListView.as_view()),
    path("<int:id>/", StudentEditView.as_view())
]
