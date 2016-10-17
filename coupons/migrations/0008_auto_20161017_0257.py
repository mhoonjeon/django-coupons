# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0007_auto_20151105_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='redeem_count',
            field=models.IntegerField(default=0, verbose_name='Redeem Count'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='redeem_limit',
            field=models.PositiveIntegerField(default=None, help_text='Leave empty for coupons that have no redeem limit', null=True, verbose_name='Redeem limit', blank=True),
        ),
    ]
