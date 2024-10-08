# Generated by Django 3.2.7 on 2024-06-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=100)),
                ('grain', models.CharField(max_length=100)),
                ('density', models.CharField(max_length=100)),
                ('durability', models.CharField(max_length=100)),
                ('uses', models.TextField()),
                ('care_instructions', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='woods/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='woods/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='woods/')),
            ],
        ),
    ]
