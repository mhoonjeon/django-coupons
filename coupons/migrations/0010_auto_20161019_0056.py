# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0009_coupon_criteria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Type', choices=[(b'monetary', b'Money based coupon'), (b'percentage', b'Percentage discount'), (b'virtual_currency', b'Virtual currency'), (b'quantity', b'Quantity based coupon')]),
        ),
    ]
