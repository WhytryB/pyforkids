from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Модель ПЕРСОНА, ТЭГ, ГРУППА
"""


class Person(models.Model):
    # Модели которые хранят основные данные пользователя, которые отображаютс в его профиле

    # Телефон пользователя
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personshop',  null=True)
    first_name = models.CharField('Имя', max_length=100, null=True, blank=False)
    second_name = models.CharField('Фамилия', max_length=100, null=True, blank=False)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    # Смс сообщение , которое присылается пользователю при входе и регистрации
    sms_mes = models.CharField('Сообщение', max_length=100, null=True, blank=True)


    def __str__(self):
        return '{second_name} {first_name} ({birthday}){sms_mes}'.format (
            first_name=self.first_name,
            second_name=self.second_name,
            birthday=self.birthday,
            sms_mes = self.sms_mes
        )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


"""
# Модель ТРАНЗАКЦИЯ, ЦЕНА , ЕДИНИЦА ИЗМЕРЕНИЯ
"""



"""
# Модель ГАЛЕРЕЯ
"""



class Galery(models.Model):
    # Модель в которой хранится соответствие персоны и его фоторгафий
    image = models.ImageField(upload_to='person_photo', null=True, blank=True, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='galery')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



