# Generated by Django 4.1.7 on 2023-04-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_alter_projetos_relatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='relatorio',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
