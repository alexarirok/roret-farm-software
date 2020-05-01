
from django.db import models
from datetime import timezone
from django.forms import ModelForm


class Livestock(models.Model):
    DAIRY = 1
    BEEF = 2
    POULTRY = 3
    SHEEP = 4
    GOATS = 5
    CAMELS = 6
    LIVESTOCK_TYPES = (
        (DAIRY, 'Dairy'),
        (BEEF, 'Beef'),
        (POULTRY, 'Poultry'),
        (SHEEP, 'Sheep'),
        (GOATS, 'Goats'),
        (CAMELS, 'Camels'),
    )

    CHOICES = (
        (11, 'Active'),
        (12, 'Butchured'),
        (13, 'Culled'),
        (14, 'Deceased'),
        (15, 'Dry'),
        (16, 'Lactating'),
        (17, 'Off Farm'),
        (18, 'Quarantined'),
        (19, 'Sickly'),
        (20, 'Sold'),
        (22, 'Weaning'),
    )

    CHOICES_1 = (
        (23, 'Quantity'),
        (24, 'Litres'),
        (25, 'Kilograms'),
        (26, 'Tons'),
        (27, 'Grams'),
        (28, 'Dozens'),
        (29, 'Bales'),
        
    )

    name = models.CharField(max_length=50)
    livestock_type = models.PositiveSmallIntegerField(choices=LIVESTOCK_TYPES)
    internal_id = models.IntegerField(null=True)
    key_words = models.CharField(max_length=50)
    status = models.PositiveSmallIntegerField(choices=CHOICES)
    breeding_stock = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    breed = models.CharField(max_length=10)
    coloring = models.CharField(max_length=10)
    retention_score = models.IntegerField(null=True)
    description = models.TextField(max_length=500)
    tag_numbers = models.IntegerField(null=True)
    other_tag_numbers = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    birth_weight = models.IntegerField(null=True)
    raised_purchased = models.CharField(max_length=10)
    veterinarian = models.CharField(max_length=10)
    on_feed = models.CharField(max_length=10)
    feed_type = models.CharField(max_length=10)
    feed_cost = models.IntegerField(null=True)
    measure_harvest = models.PositiveSmallIntegerField(choices=CHOICES_1)
    estimated_revenue = models.IntegerField(null=True)

    def __str__(self):
        return f" Livestock {self.name}"
