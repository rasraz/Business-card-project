# Generated by Django 4.1 on 2022-08-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_features_rename_about_use_myinfo_about_us_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_category',
            field=models.CharField(choices=[('I', 'Illustration'), ('AN', 'Animation'), ('AP', 'App UI'), ('W', 'Web UI'), ('S', 'Social Media'), ('P', 'Print Design')], default='A', max_length=30),
        ),
    ]
