from re import search
from chat.models import Chat, Message
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text','created_at', 'author', 'receiver')
    list_display = ('created_at', 'author', 'text', 'receiver')
    search_fields = ('text',)
# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
