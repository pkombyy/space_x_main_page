# Generated by Django 5.0.7 on 2024-07-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=40)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Feature Block',
                'verbose_name_plural': 'Feature Blocks',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
                'ordering': ['order'],
            },
        ),
    ]