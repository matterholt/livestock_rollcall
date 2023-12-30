from django.contrib import admin
from .models import Specific, History, Specie, Genealogy, Record

# Register your models here.
admin.site.register(Specific)
admin.site.register(History)
admin.site.register(Specie)
admin.site.register(Genealogy)
admin.site.register(Record)
