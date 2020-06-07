# Generated by Django 3.0.3 on 2020-05-20 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Topic'),
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Webpage')),
            ],
        ),
    ]