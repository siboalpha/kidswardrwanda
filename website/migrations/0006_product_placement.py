# Generated by Django 4.1.2 on 2022-10-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_product_priduct_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='placement',
            field=models.CharField(choices=[('recently added', 'recently added'), ('popular', 'popular')], default='popular', max_length=255),
        ),
    ]
