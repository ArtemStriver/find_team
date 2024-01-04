from django.contrib import admin
from .models import Teams, JoinInTeam


@admin.register(Teams)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(JoinInTeam)
class JoinInTeamAdmin(admin.ModelAdmin):
    pass
