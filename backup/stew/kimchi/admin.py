from django.contrib import admin
from .models import textStory

class StoryDbAdmin(admin.ModelAdmin):
    search_fields = ['text']

admin.site.register(textStory, StoryDbAdmin)
