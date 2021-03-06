# Generated by Django 3.1.5 on 2021-02-17 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GDBU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GIG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jeju',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Latlng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seoul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=7)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=7)),
                ('address', models.CharField(max_length=100)),
                ('homepage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('writedate', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
