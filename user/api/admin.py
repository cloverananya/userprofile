from django.contrib import admin

from .models import User, Profile

admin.site.register(User)
admin.site.register(Profile)

class User(admin.ModelAdmin):
    # username = 'username'
    # list_display = ['name']
    # last_filter = ('name',)
    # fieldsets = (
    #     None,{"fields":('name',)})
    pass

class Profile(admin.ModelAdmin):
    pass



