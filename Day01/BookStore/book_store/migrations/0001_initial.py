# Generated by Django 4.2.1 on 2023-06-01 08:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('views', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('isbn', models.BigAutoField(primary_key=True, serialize=False)),
                ('author_title', models.CharField(max_length=50)),
                ('book_title', models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('phone', models.CharField(max_length=15, verbose_name='phone')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('hrr', 'Horror'), ('cd', 'Comedy'), ('dra', 'Drama'), ('sci', 'Science'), ('hs', 'History')], max_length=20, validators=[django.core.validators.MinValueValidator(2)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.books')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='ISBN',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book_store.isbn'),
        ),
        migrations.AddField(
            model_name='books',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.users'),
        ),
    ]
