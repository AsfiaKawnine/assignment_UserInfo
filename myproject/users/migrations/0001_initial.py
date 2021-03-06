# Generated by Django 3.2.7 on 2021-10-02 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.parent')),
            ],
        ),
    ]
