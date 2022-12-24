from django.contrib import admin

from reports.models import Category, Report


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    search_fields = ('name', )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ('name', )

