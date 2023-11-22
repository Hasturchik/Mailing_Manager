import django
from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message_text = models.TextField()

    def __str__(self):
        return self.id


class Client(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    phone_number = models.IntegerField()  # 7XXXXXXXXXX
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)


class Message(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[('PENDING', 'Ожидается'), ('SENT', 'Успешно'),
                                       ('FAILED', 'Ошибка')], default='PENDING', max_length=10)
    mailing = models.ForeignKey(Mailing, on_delete=django.db.models.deletion.PROTECT)
    client = models.ForeignKey(Client, on_delete=django.db.models.deletion.PROTECT)
    # Add other fields as needed
    def __str__(self):
        return self.client
