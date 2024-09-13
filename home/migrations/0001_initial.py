# Generated by Django 4.2.16 on 2024-09-13 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
                ('author', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Li', 'Life'), ('Na', 'Nature'), ('Kn', 'Knowledge'), ('Mo', 'Motivation'), ('In', 'Inspiration')])),
                ('verified', models.BooleanField(default=False)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
