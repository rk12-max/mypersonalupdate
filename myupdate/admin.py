from django.contrib import admin
from .models import myupdate
# Register your models here.


@admin.register(myupdate)
class myupdateAdmin(admin.ModelAdmin):
    list_display=['title','complete','created_at']
    list_filter=['complete','created_at']
    readonly_fields=['created_at']