# Generated by Django 4.2.7 on 2023-11-10 02:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tarefas", "0002_alter_tarefa_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="descricao",
            field=models.TextField(blank=True, null=True, verbose_name="descrição"),
        ),
    ]
