# Generated by Django 3.2.4 on 2021-06-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_contato_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mensagem',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
