# Generated by Django 4.1.7 on 2023-03-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_delete_relatorios_projetos_relatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='relatorio',
            field=models.FileField(upload_to=''),
        ),
    ]
