# Generated by Django 4.1.2 on 2022-11-11 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyric_content_lyric_song_id_song_artiste_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
    ]
