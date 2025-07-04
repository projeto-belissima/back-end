# Generated by Django 5.1.7 on 2025-05-26 21:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_vestido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_medicao', models.DateField(auto_now_add=True)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('busto_altura', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura do busto')),
                ('busto_circunferencia', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Circunferência do busto')),
                ('cintura_altura', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura da cintura')),
                ('cintura_circunferencia', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Circunferência da cintura')),
                ('quadril_altura', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura do quadril')),
                ('quadril_circunferencia', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Circunferência do quadril')),
                ('costas_largura', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Largura das costas')),
                ('ombro_comprimento', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Comprimento do ombro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medidas', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emissao', models.DateTimeField(auto_now_add=True, verbose_name='Data de emissão')),
                ('status', models.IntegerField(choices=[(0, 'Encomendado'), (1, 'Iniciada produção'), (2, 'Pronto'), (3, 'Pago'), (4, 'Descartado')], default=0)),
                ('vestido_comprimento', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Comprimento do vestido')),
                ('manga_comprimento', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Comprimento da manga')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='encomendas', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('vestido', models.ManyToManyField(blank=True, related_name='encomendas', to='core.vestido')),
                ('medidas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='encomendas', to='core.medidas')),
            ],
        ),
    ]
