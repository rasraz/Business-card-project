# Generated by Django 4.1 on 2022-08-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactus_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphic_design', models.TextField()),
                ('web_design', models.TextField()),
                ('html_css', models.TextField()),
                ('ui_ux_design', models.TextField()),
                ('SEO_optimization', models.TextField()),
                ('business_development', models.TextField()),
            ],
        ),
    ]