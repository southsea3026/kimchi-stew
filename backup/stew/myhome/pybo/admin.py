from django.contrib import admin
from .models import StoryDb

# Register your models here.
class StoryDbAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(StoryDb, StoryDbAdmin)

