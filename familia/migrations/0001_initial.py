# Generated by Django 4.1.1 on 2022-09-05 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaMiembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('fecha_nacimiento', models.DateField()),
                ('peso_kg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('familia_miembro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='familia.familiamiembro')),
            ],
        ),
    ]