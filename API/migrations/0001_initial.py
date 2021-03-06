# Generated by Django 3.1.4 on 2021-07-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_category', models.CharField(choices=[('shoes', 'shoes'), ('clothes', 'clothes'), ('accessories', 'accessories')], default='shoes', max_length=100)),
                ('product_price', models.FloatField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
