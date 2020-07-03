# Generated by Django 3.0.3 on 2020-07-03 04:59

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wikimaterials',
            options={'verbose_name': 'МАТЕРИАЛ ДЛЯ СПРАВОЧНИКА', 'verbose_name_plural': 'МАТЕРИАЛЫ ДЛЯ СПРАВОЧНИКА'},
        ),
        migrations.AddField(
            model_name='dirseo',
            name='op_graph_photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/', verbose_name='ФОТО ДЛЯ OPENGRAPH'),
        ),
    ]
