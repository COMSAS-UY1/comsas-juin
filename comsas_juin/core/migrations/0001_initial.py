# Generated by Django 4.0.4 on 2022-04-22 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('begin_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('status', models.CharField(choices=[('programmed', 'programmed'), ('active', 'active')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_title', models.CharField(max_length=255)),
                ('small_title', models.CharField(max_length=255)),
                ('background', models.ImageField(upload_to='images/slides/')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='images/speakers/')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkdin', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('about', models.TextField()),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.edition')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='images/partners/')),
                ('web_site', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.TextField()),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.edition')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flyers', models.ImageField(upload_to='images/events/')),
                ('location', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('directed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.speaker')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.edition')),
            ],
        ),
    ]
