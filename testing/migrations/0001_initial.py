# Generated by Django 4.0.2 on 2022-02-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Task', models.TextField(max_length=1000)),
                ('Due_Date', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['Due_Date'],
            },
        ),
    ]
