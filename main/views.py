from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student


def index(request):
    context = {
        'objects_list': Student.objects.all()[:3],
        'title': 'Главная'
    }

    return render(request, "main/index.html", context)


class StudentListView(ListView):
    model = Student
    # template_name = 'main/student_list.html'


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'main/student_detail.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(
            f'user {name} with email {email} send message: {message}'
        )

    context = {
        'title': 'Контакты'
    }

    return render(request, "main/contact.html", context)


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'surname', 'avatar')
    success_url = reverse_lazy('main:students_list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'surname', 'avatar')
    success_url = reverse_lazy('main:students_list')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:students_list')
