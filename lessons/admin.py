from django.contrib import admin

from .models import *

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Material)
admin.site.register(Message)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Subject)