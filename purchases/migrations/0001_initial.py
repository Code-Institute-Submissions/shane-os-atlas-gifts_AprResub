# Generated by Django 3.2.8 on 2022-02-12 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=128)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('address_line3', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pre_discount_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('final_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('sub_total', models.DecimalField(decimal_places=2, editable=False, max_digits=5)),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifts.gift')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_purchase', to='purchases.purchase')),
            ],
        ),
    ]
