# Generated by Django 4.1.7 on 2023-03-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_alter_ordem_serviço_descrição'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_serviço',
            name='situação',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='ordem_serviço',
            name='tipo_serviço',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='situação',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='tipo_serviço',
            field=models.CharField(max_length=100),
        ),
    ]
