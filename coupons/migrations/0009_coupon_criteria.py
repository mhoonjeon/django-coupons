# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0008_auto_20161017_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='criteria',
            field=models.IntegerField(help_text='Arbitrary coupon criteria amount that must be met for the coupon to be valid', null=True, verbose_name='Criteria', blank=True),
        ),
    ]
