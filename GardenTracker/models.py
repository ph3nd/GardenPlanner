from django.db import models
from django.utils.translation import gettext_lazy as _

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
    botanical_name = models.CharField(max_length=256)
    description = models.TextField()
    germination_days = models.IntegerField()
    pot_on_days = models.IntegerField()
    transplant_days = models.IntegerField()
    first_harvest_days = models.IntegerField()
    harvest_type = models.IntegerField(choices=HarvestChoices.choices, default=HarvestChoices.HARVEST_SINGLE)
    preferred_sun = models.IntegerField(choices=PreferredSun.choices, default=PreferredSun.SUN_FULL)


class Plant(models.Model):
    
    seed = models.ForeignKey('Seed', on_delete=models.PROTECT)
    soil_description = models.TextField()
    quantity = models.IntegerField()
    sow_date = models.DateField()
    germinate_date = models.DateField()
    pot_on_date = models.DateField()
    transplant_date = models.DateField()
    first_harvest_date = models.DateField()
    last_harvest_date = models.DateField()
    harvested = models.BooleanField(default=False)
    total_yield = models.IntegerField(help_text='Yield in KG')


class Note(models.Model):

    seed_id = models.ForeignKey('Seed', on_delete=models.CASCADE)
    plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='notes/')

