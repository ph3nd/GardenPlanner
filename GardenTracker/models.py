from django.db import models

# Create your models here.

class Seed(models.Model):
    class HarvestChoices(models.TextChoice):
        HARVEST_SINGLE = 1, _('Single Harvest')
        HARVEST_CONTINUOUS = 2, _('Continuous Harvest')
        HARVEST_MULTIPLE = 3, _('Multiple Harvest')

    class PreferredSun(models.TextChoice):
        SUN_FULL = 1, _('Full Sun')
        SUN_PART = 2, _('Sun/Shade')
        SUN_SHADE = 3, _('Shade')

    common_name = models.CharField()
    botanical_name = models.CharField()
    description = models.TextField()
    germination_days = models.IntegerField()
    pot_on_days = models.IntegerField()
    transplant_days = models.IntegerField()
    first_harvest_days = models.IntegerField()
    harvest_type = models.IntegerField(choices=HarvestChoices.choices, default=HarvestChoices.HARVEST_SINGLE)
    prefered_sun = models.IntegerField(choices=PreferedSun.choices, default=PreferedSun.SUN_FULL)


class Plant(models.Model):
    
    seed = models.ForeignKey('Seed', on_delete=models.PROTECT)
    soil_description = models.TextField()
    sow_date = models.DateField()
    germinate_date = models.DateField()
    pot_on_date = models.DateField()
    transplant_date = models.DateField()
    first_harvest_date = models.DateField()
    last_harvest_date = models.DateField()


class Note(models.Model):

    seed_id = models.ForeignKey('Seed', on_delete=models.CASCADE)
    plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE)

