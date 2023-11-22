from django.contrib import admin
from .models import Mailing, Client, Message

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'message_text')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'operator_code', 'tag', 'timezone')
    search_fields = ['phone_number']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'status', 'mailing', 'client')
    list_filter = ('status', 'mailing')
    search_fields = ['client__phone_number']