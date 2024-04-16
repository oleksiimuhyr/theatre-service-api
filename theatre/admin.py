from django.contrib import admin

from theatre.models import Play


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    pass
