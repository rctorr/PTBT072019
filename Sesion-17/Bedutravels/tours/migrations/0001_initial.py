# Generated by Django 3.0.3 on 2020-03-04 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=256)),
                ('fechaNacimiento', models.DateField()),
                ('clave', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('genero', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro'), ('N', 'Prefiero no indicarlo')], max_length=1)),
            ],
        ),
    ]
