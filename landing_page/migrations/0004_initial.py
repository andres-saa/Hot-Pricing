# Generated by Django 4.2.1 on 2023-05-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing_page', '0003_delete_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=400)),
                ('image', models.URLField(max_length=400)),
                ('tittle', models.CharField(max_length=50)),
            ],
        ),
    ]
