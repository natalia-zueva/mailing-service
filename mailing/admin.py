from django.contrib import admin

from mailing.models import Client, Message, Mailing, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'surname', 'comment',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_start', 'time_end', 'period', 'status', 'message',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'status', 'response', 'mailing',)
