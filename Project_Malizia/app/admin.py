

from django.contrib import admin

from app.models import Features


# Register your models here.
@admin.register(Features)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)