# Generated by Django 3.2.7 on 2021-09-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('QUARTER', 'Quarter')], default='QUARTER', max_length=20)),
            ],
        ),
    ]
