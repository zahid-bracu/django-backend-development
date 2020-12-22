# Generated by Django 3.1.4 on 2020-12-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent')]),
        ),
        migrations.AlterField(
            model_name='musician',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]