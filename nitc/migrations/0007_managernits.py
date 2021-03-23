# Generated by Django 3.1.7 on 2021-03-12 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nitc', '0006_auto_20210312_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerNITS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('wdate', models.DateField()),
                ('phone', models.CharField(max_length=50)),
                ('passport_seria', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('inn', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('inps', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('diplom', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('turdavoy', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('obyektivka', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nitc.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
