# Generated by Django 3.2.9 on 2022-03-28 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0010_alter_character_ilevel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='raid',
        ),
        migrations.AddField(
            model_name='member',
            name='raid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='guild.raidgroup'),
        ),
    ]
