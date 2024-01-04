from django.contrib import admin

from users.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
