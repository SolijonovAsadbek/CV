from django.contrib import admin


# Register your models here.
from my_cv.models import Head


class HeadAdmin(admin.ModelAdmin):
    list_display = ['hi', 'fullname', 'about', 'button']


admin.site.register(Head, HeadAdmin)
