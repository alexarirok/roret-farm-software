# Generated by Django 3.0.5 on 2020-04-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livestock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('livestock_type', models.PositiveSmallIntegerField(choices=[(1, 'Dairy'), (2, 'Beef'), (3, 'Poultry'), (4, 'Sheep'), (5, 'Goats'), (6, 'Camels')])),
                ('internal_id', models.IntegerField(null=True)),
                ('key_words', models.CharField(max_length=50)),
                ('status', models.PositiveSmallIntegerField(choices=[(11, 'Active'), (12, 'Butchured'), (13, 'Culled'), (14, 'Deceased'), (15, 'Dry'), (16, 'Lactating'), (17, 'Off Farm'), (18, 'Quarantined'), (19, 'Sickly'), (20, 'Sold'), (22, 'Weaning')])),
                ('breeding_stock', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=10)),
                ('coloring', models.CharField(max_length=10)),
                ('retention_score', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=500)),
                ('tag_numbers', models.IntegerField(null=True)),
                ('other_tag_numbers', models.IntegerField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('birth_weight', models.IntegerField(null=True)),
                ('raised_purchased', models.CharField(max_length=10)),
                ('veterinarian', models.CharField(max_length=10)),
                ('on_feed', models.CharField(max_length=10)),
                ('feed_type', models.CharField(max_length=10)),
                ('feed_cost', models.IntegerField(null=True)),
                ('measure_harvest', models.PositiveSmallIntegerField(choices=[(23, 'Quantity'), (24, 'Litres'), (25, 'Kilograms'), (26, 'Tons'), (27, 'Grams'), (28, 'Dozens'), (29, 'Bales')])),
                ('estimated_revenue', models.IntegerField(null=True)),
            ],
        ),
    ]
