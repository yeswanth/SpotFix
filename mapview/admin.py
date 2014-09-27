from django.contrib import admin
from models import Tag,Issue

class TagAdmin(admin.ModelAdmin):
    pass

class IssueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag,TagAdmin) 
admin.site.register(Issue,IssueAdmin) 

