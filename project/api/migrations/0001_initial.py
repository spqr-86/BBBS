# Generated by Django 3.2.3 on 2021-05-28 08:16

import colorfield.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import api.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Город')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Приоритет вывода')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес мероприятия')),
                ('contact', models.CharField(max_length=200, verbose_name='Контактное лицо')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание мероприятия')),
                ('start_at', models.DateTimeField(verbose_name='Время начала')),
                ('end_at', models.DateTimeField(verbose_name='Время окончания')),
                ('seats', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Максимальное число участников')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='api.city', verbose_name='Город мероприятия')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ('id',),
                'permissions': (('view_all_cities', 'Можно смотреть события всех городов'),),
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заглавие')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('info', models.CharField(max_length=500, verbose_name='Информация')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Изображение')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг (Ссылка)')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('info', models.TextField(max_length=512, verbose_name='Информация')),
                ('image_url', models.URLField(max_length=192, verbose_name='Ссылка на изображение')),
                ('link', models.URLField(max_length=192, verbose_name='Ссылка на видеоролик')),
                ('duration', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(86400)], verbose_name='Продолжительность видеоролика в сек.')),
            ],
            options={
                'verbose_name': 'Видеоролик',
                'verbose_name_plural': 'Видеоролики',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('tags', models.ManyToManyField(related_name='questions', to='api.Tag', verbose_name='Тег(и)')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_region_moderator', models.BooleanField(default=False, verbose_name='Региональный модератор')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='api.city', verbose_name='Город')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event', validators=[api.validators.events_lifetime_validator, api.validators.free_seats_validators])),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Запись на событие',
                'verbose_name_plural': 'Записи на события',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('info', models.TextField(max_length=512, verbose_name='Информация')),
                ('image_url', models.URLField(max_length=192, verbose_name='Ссылка на изображение')),
                ('link', models.URLField(max_length=192, verbose_name='Ссылка на фильм')),
                ('tags', models.ManyToManyField(blank=True, related_name='movies', to='api.Tag', verbose_name='Тег(и)')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('articles', models.ManyToManyField(to='api.Article', verbose_name='Статьи')),
                ('events', models.ManyToManyField(to='api.Event', verbose_name='События')),
                ('histories', models.ManyToManyField(to='api.History', verbose_name='Истории')),
                ('movies', models.ManyToManyField(to='api.Movie', verbose_name='Фильмы')),
                ('places', models.ManyToManyField(to='api.Place', verbose_name='Места')),
                ('questions', models.ManyToManyField(to='api.Question', verbose_name='Вопросы')),
                ('video', models.ManyToManyField(to='api.Video', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='events', through='api.Participant', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
        migrations.AddConstraint(
            model_name='participant',
            constraint=models.UniqueConstraint(fields=('event', 'participant'), name='event_participant_uniquetogether'),
        ),
    ]
