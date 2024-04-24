# Generated by Django 4.2.5 on 2023-09-11 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('broker', '0013_alter_transaction_number_alter_transactionone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('btc', models.CharField(default='4', max_length=200)),
                ('eth', models.CharField(default='-', max_length=200)),
                ('usdt', models.CharField(default='-', max_length=200)),
                ('usdc', models.CharField(default='-', max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
