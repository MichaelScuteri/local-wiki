# Generated by Django 5.0.7 on 2024-09-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_rename_wikiimages_wikiimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='wiki_images/'),
        ),
        migrations.DeleteModel(
            name='WikiImage',
        ),
    ]
