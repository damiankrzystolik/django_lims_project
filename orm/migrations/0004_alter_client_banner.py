# Generated by Django 5.0.6 on 2024-06-09 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_delete_enterprise_client_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='banner',
            field=models.ImageField(blank=True, default='aaa.jpg', upload_to=''),
        ),
    ]
