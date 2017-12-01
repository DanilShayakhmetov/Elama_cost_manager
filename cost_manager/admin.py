from django.contrib import admin
from .models import Post

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'



class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Post)
