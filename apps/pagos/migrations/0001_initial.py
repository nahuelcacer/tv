# Generated by Django 4.1.1 on 2022-10-16 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('periodo', '0001_initial'),
        ('clientes', '0002_alter_cliente_suscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe', models.IntegerField()),
                ('fecha', models.DateField(null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='periodo.periodo')),
            ],
        ),
    ]
