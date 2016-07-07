# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='core_num',
            field=models.SmallIntegerField(null=True, choices=[(2, b'2 Cores'), (4, b'4 Cores'), (6, b'6 Cores'), (8, b'8 Cores'), (10, b'10 Cores'), (12, b'12 Cores'), (14, b'14 Cores'), (16, b'16 Cores'), (18, b'18 Cores'), (20, b'20 Cores'), (22, b'22 Cores'), (24, b'24 Cores'), (26, b'26 Cores'), (28, b'28 Cores'), (30, b'30 Cores'), (32, b'32 Cores'), (34, b'34 Cores'), (36, b'36 Cores')]),
            preserve_default=True,
        ),
    ]
