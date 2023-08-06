from django.urls import path

from main.apps import MainConfig
from main.views import index, contacts, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('students/', StudentListView.as_view(), name='students_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_item'),
    path('activity/<int:pk>/', toggle_activity, name='activity_student')
]
