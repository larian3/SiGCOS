# Generated by Django 4.1.7 on 2023-03-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_alter_ordem_serviço_situação_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='relatorio',
            field=models.FileField(default='null', upload_to='pdf/'),
            preserve_default=False,
        ),
    ]
