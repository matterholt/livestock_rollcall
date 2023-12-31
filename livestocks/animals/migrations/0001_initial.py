# Generated by Django 4.2.8 on 2023-12-30 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specific',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=200)),
                ('animal_id', models.CharField(help_text='any way to ID the lamb visually name or number', max_length=200, unique=True)),
                ('birth_date', models.CharField(max_length=200)),
                ('sibling_set', models.CharField(help_text='born as single (1), twin(2), triplet(3)', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(help_text='the type of livestock animal', max_length=200, unique=True)),
                ('breed', models.CharField(help_text='from the specie what name of breed', max_length=200, unique=True)),
                ('animal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='animals.specific')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('s', 'sold'), ('i', 'ill'), ('r', 'roster'), ('p', 'purchased'), ('d', 'delivered')], default='r', max_length=1)),
                ('notes', models.CharField(max_length=500)),
                ('animal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='animals.specific')),
            ],
        ),
    ]
