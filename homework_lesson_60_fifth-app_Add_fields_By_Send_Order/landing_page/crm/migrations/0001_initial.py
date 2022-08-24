# Generated by Django 4.0.7 on 2022-08-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('order_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('order_phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('order_whats_happen', models.CharField(max_length=200, verbose_name='Причина неисправности')),
                ('order_service_name', models.CharField(max_length=200, verbose_name='Название услуги')),
                ('order_not_work', models.CharField(max_length=200, verbose_name='Что не работает')),
                ('order_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='CommentsCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('comment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
