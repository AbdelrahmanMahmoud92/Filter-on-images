# Generated by Django 5.0.1 on 2024-01-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('action', models.CharField(choices=[('NO_FILTER', 'no_filter'), ('COLORIEZD', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BRURRED', 'blurred')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]