# Generated by Django 4.2.7 on 2023-11-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "bibliotecas_python",
            "0002_alter_bibliotecas_ano_alter_bibliotecas_criador_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="bibliotecas",
            name="ano",
            field=models.IntegerField(
                blank=True, max_length=200, null=True, verbose_name="ano de Criação"
            ),
        ),
    ]
