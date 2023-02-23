# Generated by Django 4.1.5 on 2023-02-23 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('photoBook', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photoAuthor', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rentalPriceDay', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rentalPeriod', models.IntegerField(blank=True, null=True)),
                ('totalRental', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('availble', 'availble'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lms_app.category')),
            ],
        ),
    ]