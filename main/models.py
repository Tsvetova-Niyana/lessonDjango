from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Student(models.Model):
    """ формирование модели для дальнейшей работы с БД
          в settings.py надо подключить media_url и media_root
          в urls.py основной надо подключить media_url и media_root (добавить static(settings.MEDIA_URL,
          document_root=settings.MEDIA_ROOT)). При подключении static использовать django.conf.static.static()
          При подключении settings использовать django.conf.settings"""
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')

    """ для работы с изображениями необходимо поставить пакет pip install pillow
        upload_to='' настройка для указания куда будет загружаться изображение относительно папки
        null=True, blank=True значит, что в БД может быть пустое поле, т.е. необязательное к заполнению"""

    # avatar = models.ImageField(upload_to='students/', verbose_name='Аватарка', null=True, blank=True)

    # через распаковку(в случае если notnull у многих полей)
    avatar = models.ImageField(upload_to='students/', verbose_name='Аватарка', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='активный')

    """чтобы попасть в админпанель переходим  http://127.0.0.1:8000/admin
    через терминал создаем суперпользователя для подключения. Команда - python manage.py createsuperuser
    далее вводим логин и пароль.
    Далее можно логиниться"""


    def __str__(self):
        return f'{self.first_name} {self.surname}'

    # дополнительная информация
    class Meta:
        # Название модели по-русски
        verbose_name = 'Студент'

        # Название модели по-русски во множественном числе
        verbose_name_plural = 'Студенты'

        # Формирование порядка сортировки по возрастанию (по убыванию ordering = ('-surname'))
        ordering = ('surname',)
