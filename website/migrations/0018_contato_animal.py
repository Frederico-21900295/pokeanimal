# Generated by Django 3.2.4 on 2021-06-18 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20210618_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='animal',
            field=models.CharField(choices=[('Alce', 'Alce'), ('Chita', 'Chita'), ('Cão', 'Cão'), ('Gato', 'Gato'), ('Leão', 'Leão'), ('Leopardo', 'Leaopardo'), ('Orca', 'Orca'), ('Tigre', 'Tigre'), ('Touro', 'Touro'), ('Tubarão', 'Tubarão')], default='Cao', max_length=10),
        ),
    ]