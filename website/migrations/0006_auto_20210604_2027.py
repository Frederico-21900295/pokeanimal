# Generated by Django 3.2.3 on 2021-06-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210604_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resposta',
            name='respostas',
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas10',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas5',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas6',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas7',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas8',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='resposta',
            name='respostas9',
            field=models.CharField(default='', max_length=20),
        ),
    ]