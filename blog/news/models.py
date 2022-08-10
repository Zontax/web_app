from django.db import models


class Artiles(models.Model):
    '''Класс таблиці новин в бд'''
    class Meta:
        '''Підклас зміни назви таблиці в адмін панелі'''
        verbose_name = 'Новину'
        verbose_name_plural = 'Новини'

    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Публікація')
    date = models.DateTimeField('Дата публікації')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title # Вивід публікацій з бд
