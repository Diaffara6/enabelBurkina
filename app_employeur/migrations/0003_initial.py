# Generated by Django 4.2.3 on 2023-08-19 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_employeur', '0002_delete_employeur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fonction', models.CharField(blank=True, max_length=40)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
