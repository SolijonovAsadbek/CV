from django.contrib import admin

# Register your models here.
from my_cv.models import Head, About, Skills


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1


class HeadAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'button']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['subject', 'create_date']
    inlines = [SkillsInline]


admin.site.register(Head, HeadAdmin)
admin.site.register(About, AboutAdmin)
