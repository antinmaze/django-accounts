# Generated by Django 4.1 on 2022-09-27 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a category of good', max_length=200)),
                ('code', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this category of good')),
                ('description', models.TextField(help_text='description of the Category', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a OwnerGroup of good', max_length=200)),
                ('code', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this OwnerGroup of good')),
                ('url', models.URLField()),
                ('createdat', models.TimeField(auto_now_add=True)),
                ('updatedat', models.TimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a subcategory of good', max_length=200)),
                ('code', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this subcategory of good')),
                ('description', models.TextField(help_text='description of the SubCategory', max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.category')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isadmin', models.BooleanField()),
                ('code', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this OwnerGroup of good')),
                ('createdat', models.TimeField(auto_now_add=True)),
                ('updatedat', models.TimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
                ('ownergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.ownergroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Good item', max_length=200)),
                ('summary', models.TextField(help_text='summary of the Good', max_length=300)),
                ('description', models.TextField(help_text='description of the Good', max_length=1000)),
                ('code', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this OwnerGroup of good')),
                ('url', models.URLField()),
                ('status', models.CharField(choices=[('AV', 'Available'), ('OT', 'Out'), ('BK', 'Booked'), ('CA', 'Canceled'), ('CN', 'Confirmed'), ('CM', 'Completed')], default='AV', help_text='Status a Good item', max_length=2)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('state', models.CharField(choices=[('N', 'New Condition'), ('V', 'Very Good State'), ('G', 'Good State'), ('S', 'Satisfactory State')], default='N', help_text='State of a Good item', max_length=1)),
                ('createdat', models.TimeField(auto_now_add=True)),
                ('updatedat', models.TimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.category')),
                ('ownergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.ownergroup')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.subcategory')),
            ],
        ),
    ]