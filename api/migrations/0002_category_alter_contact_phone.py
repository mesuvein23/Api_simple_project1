# Generated by Django 4.2.9 on 2024-03-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_slug', models.CharField(max_length=100)),
                ('c_image', models.ImageField(default='', null=True, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
