# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20160707_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=64, verbose_name='\u4e3b\u673a\u540d', db_index=True),
            preserve_default=True,
        ),
    ]
