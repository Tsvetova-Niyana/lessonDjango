from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Олег', 'surname': 'Маслов'},
            {'first_name': 'Алексей', 'surname': 'Матюк'},
            {'first_name': 'Юлия', 'surname': 'Блохина'}
        ]

        student_objects = []
        for student in student_list:
            student_objects.append(Student(**student))

        Student.objects.bulk_create(student_objects)