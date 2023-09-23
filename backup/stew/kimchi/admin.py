from django.contrib import admin
from .models import StoryDb, Total

class StoryDbAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(StoryDb, StoryDbAdmin)
admin.site.register(Total)