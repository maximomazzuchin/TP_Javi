from django.contrib import admin
from TPN2.models import Descuentos

# Register your models here.


class DescuentosAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_from', 'valid_to', 'discount', 'available')


admin.site.register(Descuentos, DescuentosAdmin)