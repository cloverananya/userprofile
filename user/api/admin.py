from django.contrib import admin

from .models import User, Profile

admin.site.register(User)
admin.site.register(Profile)


class User(admin.ModelAdmin):
    pass


class Profile(admin.ModelAdmin):
    pass



