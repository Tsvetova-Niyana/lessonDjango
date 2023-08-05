from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Student


def index(request):
    context = {
        'objects_list': Student.objects.all()[:3],
        'title': 'Главная'
    }

    return render(request, "main/index.html", context)


class StudentListView(ListView):
    model = Student
    template_name = 'main/students.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student.html'


# def student(request, pk):
#     student_item = Student.objects.get(pk=pk)
#
#     context = {
#         'object': student_item,
#         'title': student_item
#     }
#
#     return render(request, 'main/student.html', context)


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
