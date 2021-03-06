# Generated by Django 3.0.3 on 2020-07-02 17:49

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priceseo',
            options={'verbose_name': 'SEO ДЛЯ СТРАНИЦЫ "ПРАЙС-ЛИСТ"', 'verbose_name_plural': 'SEO ДЛЯ СТРАНИЦЫ "ПРАЙС-ЛИСТ"'},
        ),
        migrations.AddField(
            model_name='priceseo',
            name='op_graph_photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/', verbose_name='ФОТО ДЛЯ OPENGRAPH'),
        ),
    ]
