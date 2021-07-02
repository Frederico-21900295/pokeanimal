# Generated by Django 3.2.4 on 2021-06-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20210607_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario_values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Excelente', models.IntegerField(default=0)),
                ('Muito_Bom', models.IntegerField(default=0)),
                ('Bom', models.IntegerField(default=0)),
                ('Mau', models.IntegerField(default=0)),
                ('Pessimo', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Pontos_clareza',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Pontos_design',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Pontos_originalidade',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Pontos_rigor',
        ),
    ]
