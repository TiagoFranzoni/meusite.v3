# Generated by Django 4.2.7 on 2023-11-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bibliotecas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(max_length=200, verbose_name="nome da Biblioteca"),
                ),
                (
                    "ano",
                    models.CharField(max_length=200, verbose_name="ano de Criação"),
                ),
                ("descricao", models.TextField(verbose_name="descrição")),
                (
                    "criador",
                    models.CharField(max_length=200, verbose_name="nome do criardor"),
                ),
                (
                    "mantenedor",
                    models.CharField(max_length=200, verbose_name="nome do mantenedor"),
                ),
                (
                    "openSource",
                    models.BooleanField(default=False, verbose_name="Open-Source"),
                ),
                ("link", models.URLField(verbose_name="link da Biblioteca")),
            ],
            options={
                "verbose_name": "Biblioteca",
                "verbose_name_plural": "Bibliotecas",
                "ordering": ["nome"],
            },
        ),
    ]
