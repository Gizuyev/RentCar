# Generated by Django 4.2.5 on 2023-09-07 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_carmake_alter_blog_options_alter_callback_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Модель')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.carmark'),
        ),
        migrations.DeleteModel(
            name='CarMake',
        ),
    ]
