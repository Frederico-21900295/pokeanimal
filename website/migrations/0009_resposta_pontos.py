# Generated by Django 3.2.3 on 2021-06-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_rename_respostas1_resposta_respostas'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='pontos',
            field=models.IntegerField(default=0),
        ),
    ]
