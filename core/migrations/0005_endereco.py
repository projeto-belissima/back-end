# Generated by Django 5.1.7 on 2025-05-19 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_email_alter_user_passage_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9)),
                ('numero', models.ImageField(blank=True, null=True, upload_to='')),
                ('logradouro', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
