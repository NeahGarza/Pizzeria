# Generated by Django 3.2 on 2021-05-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20210501_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza_type',
            field=models.CharField(choices=[('C', 'Cheese'), ('H', 'Hawaiian'), ('M', 'MeatLovers'), ('P', 'Pepperoni'), ('S', 'Supreme')], default=None, max_length=1),
        ),
    ]
