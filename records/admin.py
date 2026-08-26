from django.contrib import admin

# Register your models here.
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('pet', 'target_date', 'created_at')
    list_filter = ('target_date', 'pet')
    search_fields = ('pet__name',)