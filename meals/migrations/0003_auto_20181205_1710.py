# Generated by Django 2.1.4 on 2018-12-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='meals',
            field=models.ManyToManyField(blank=True, null=True, related_name='meals', to='meals.Meal'),
        ),
    ]
