# Generated by Django 3.2.4 on 2021-06-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_rename_comment_comentario_comentário'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_nascimento',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]