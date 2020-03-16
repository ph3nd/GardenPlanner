from django.contrib import admin
from .models import Seed, Plant, Note, Soil

# Register your models here.

admin.site.register(Seed)
admin.site.register(Plant)
admin.site.register(Note)
admin.site.register(Soil)
