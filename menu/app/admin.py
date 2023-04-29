from django.contrib import admin
from .models import MainMenu, TreeMenu


class MainMenuAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class TreeMenuAdmin(admin.ModelAdmin):
    list_display = ['main_menu', 'path', 'parent']


admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(TreeMenu, TreeMenuAdmin)
