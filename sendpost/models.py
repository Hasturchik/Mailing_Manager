# import json
import json
import time
import datetime as dt

import django
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone
import requests
from pytz import utc


class Mailing(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message_text = models.TextField()




class Client(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    phone_number = models.IntegerField()  # 7XXXXXXXXXX
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)


class Message(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    mailing = models.ForeignKey(Mailing, on_delete=django.db.models.deletion.PROTECT)
    client = models.ForeignKey(Client, on_delete=django.db.models.deletion.PROTECT)
    # Add other fields as needed
    # def __str__(self):
    #     return self.client


#         if now_time >= m.start_time :
#             print("Hello World")
#             if dt.datetime.now() >= m.start_time and dt.datetime.now() <= m.end_time
#     mailing_list = Mailing.objects.all().filter(Mailing.start_time)
#     for mail in mailing_list:
#         if mailing_list[mail] == dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"):
#             None
#         #     print("HELLO WORLD")
#             # response = requests.post('https://probe.fbrq.cloud/v1/send/MSgID', headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA5MTAwMzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9OaXlhcmxhdGhvdGVwIn0.cAK7PV6uJLORH5yPWj3WnHChiKQbORpNau2YoKhYCVI'}, json={'id':Message.id})
# print("Send")
def send():
    url = "https://probe.fbrq.cloud/v1/send/"
    data = {
        "id" : Mailing.id,
        "phone": Client.phone_number,
        "text": Mailing.message_text
    }
    response = requests.post(url, data=data, headers={
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA5MTAwMzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9OaXlhcmxhdGhvdGVwIn0.cAK7PV6uJLORH5yPWj3WnHChiKQbORpNau2YoKhYCVI"})



# while True:
#        send()
#        time.sleep(60*5) #every five min
send()









# class Mailing(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     message_text = models.TextField()
#
#     def __str__(self):
#         return self.id

# @receiver(post_save, sender=Mailing)
# def update_api_on_mailing_change(sender, instance, **kwargs):
#     headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA5MTAwMzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9OaXlhcmxhdGhvdGVwIn0.cAK7PV6uJLORH5yPWj3WnHChiKQbORpNau2YoKhYCVI"}
#     url = 'https://probe.fbrq.cloud/v1/send/' + str(Mailing.id)
#     data = {
#         'id': instance.id,
#         'start_time': instance.start_time,
#         'end_time': instance.end_time,
#         'message_text': instance.message_text,
#     }
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     if response.status_code == 200:
#         print('Changes updated in API')
#     else:
#         print('Failed to update changes in API')


# @receiver(post_save, sender=Mailing)
# def update_api_on_mailing_change(sender, instance, **kwargs):
#     header = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA5MTAwMzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9OaXlhcmxhdGhvdGVwIn0.cAK7PV6uJLORH5yPWj3WnHChiKQbORpNau2YoKhYCVI"}
#     url = 'https://probe.fbrq.cloud/v1/send/MSgID'
#     data = {
#         'id': instance.id,
#         'start_time': instance.start_time,
#         'end_time': instance.end_time,
#         'message_text': instance.message_text,
#     }
#     response = requests.put(url, data=data)
#     if response.status_code == 200:
#         print('Changes updated in API')
#     else:
#         print('Failed to update changes in API')
