from django.contrib import admin
from .models import CarModel, CarMake


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1


class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "year")


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [CarModelInline]


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
