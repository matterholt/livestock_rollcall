from django.contrib import admin
from .models import Specific, History, Specie, Genealogy, Record

# Register your models here.
admin.site.register(Specie)
# admin.site.register(Specific)
# admin.site.register(History)
admin.site.register(Genealogy)
# admin.site.register(Record)


class SpecificAdmin(admin.ModelAdmin):
    list_display = ("animal_id", "birth_date", "gender")


class HistoryAdmin(admin.ModelAdmin):
    list_filter = ("status", "animal_id")


class RecordAdmin(admin.ModelAdmin):
    fields = ["animal_id", ("action", "value")]


admin.site.register(Specific, SpecificAdmin)
admin.site.register(History, HistoryAdmin)

admin.site.register(Record, RecordAdmin)
