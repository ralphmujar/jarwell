# Generated by Django 2.2.3 on 2019-09-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0018_remove_orderitem_bulk_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_status',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='OrderSummary',
        ),
    ]
