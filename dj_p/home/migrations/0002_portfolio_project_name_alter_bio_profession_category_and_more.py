# Generated by Django 4.1 on 2022-08-14 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project_name',
            field=models.CharField(default='hello', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bio',
            name='profession_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bio', to='home.professioncategory'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='protfolio', to='home.portfoliocategory'),
        ),
    ]