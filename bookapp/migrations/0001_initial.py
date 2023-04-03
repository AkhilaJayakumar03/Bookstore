# Generated by Django 4.1.5 on 2023-03-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookupmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('bookimage', models.FileField(upload_to='bookapp/static')),
                ('date', models.DateField(auto_now_add=True)),
                ('bookpdf', models.FileField(upload_to='bookapp/static')),
            ],
        ),
    ]
