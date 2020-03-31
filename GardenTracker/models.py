from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.

class Seed(models.Model):
    class HarvestChoices(models.TextChoices):
        HARVEST_SINGLE = 1, _('Single Harvest')
        HARVEST_CONTINUOUS = 2, _('Continuous Harvest')
        HARVEST_MULTIPLE = 3, _('Multiple Harvest')

    class PreferredSun(models.TextChoices):
        SUN_FULL = 1, _('Full Sun')
        SUN_PART = 2, _('Sun/Shade')
        SUN_SHADE = 3, _('Shade')

    common_name = models.CharField(max_length=256)
    botanical_name = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    germination_days = models.IntegerField(null=True, blank=True)
    pot_on_days = models.IntegerField(null=True, blank=True)
    transplant_days = models.IntegerField(null=True, blank=True)
    first_harvest_days = models.IntegerField(null=True, blank=True)
    harvest_type = models.IntegerField(choices=HarvestChoices.choices, default=HarvestChoices.HARVEST_SINGLE)
    preferred_sun = models.IntegerField(choices=PreferredSun.choices, default=PreferredSun.SUN_FULL)
    preferred_soil = models.ForeignKey('Soil', on_delete=models.PROTECT, null=True, blank=True)


class Plant(models.Model):
    seed = models.ForeignKey('Seed', on_delete=models.PROTECT)
    soil_description = models.TextField()
    quantity = models.IntegerField()
    sow_date = models.DateField(default=datetime.date.today)
    germinate_date = models.DateField(null=True, blank=True)
    pot_on_date = models.DateField(null=True, blank=True)
    transplant_date = models.DateField(null=True, blank=True)
    first_harvest_date = models.DateField(null=True, blank=True)
    last_harvest_date = models.DateField(null=True, blank=True)
    harvested = models.BooleanField(default=False, null=True, blank=True)
    total_yield = models.IntegerField(help_text='Yield in KG', null=True, blank=True)

    def __str__(self):
        return '{0} planted on {1}'.format(self.seed.common_name, self.sow_date)


class Note(models.Model):
    seed_id = models.ForeignKey('Seed', on_delete=models.CASCADE, null=True, blank=True)
    plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='notes/', null=True, blank=True)

class Soil(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    pH = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
