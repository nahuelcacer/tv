# Generated by Django 4.1.1 on 2022-10-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(null=True)),
                ('fin', models.DateField(null=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
    ]
