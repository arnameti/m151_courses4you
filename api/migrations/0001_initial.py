# Generated by Django 3.1.2 on 2020-11-12 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plz', models.CharField(max_length=4)),
                ('ortsname', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=512)),
                ('place_fk', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.place')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschreibung', models.CharField(max_length=1024)),
                ('provider_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.provider')),
                ('course_student', models.ManyToManyField(related_name='course_student', to='api.Student')),
                ('teacher_fk', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='place_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.place'),
        ),
    ]
