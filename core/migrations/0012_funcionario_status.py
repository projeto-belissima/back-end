# Generated by Django 5.1.7 on 2025-06-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_medidas_options_alter_encomenda_emissao'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='status',
            field=models.IntegerField(choices=[(0, 'Ativo'), (1, 'Em férias'), (2, 'Afastado'), (3, 'Em treinamento'), (4, 'Inativo')], default=0),
        ),
    ]
