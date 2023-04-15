# Generated by Django 4.1.7 on 2023-03-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_fornecedores_clientes_pais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetos',
            name='orgão',
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='razão_social',
        ),
        migrations.AddField(
            model_name='projetos',
            name='descrição',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
