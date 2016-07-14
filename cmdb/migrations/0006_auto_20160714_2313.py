# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_auto_20160714_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='service_type',
            field=models.CharField(db_index=True, max_length=32, choices=[(b'app', 'app'), (b'job', 'job'), (b'mysql', 'mysql'), (b'codis', 'codis'), (b'zookeeper', 'zookeeper'), (b'dubbo', 'dubbo'), (b'lts', 'lts'), (b'rocketmq', 'rocketmq'), (b'elk', 'elk'), (b'cat', 'cat'), (b'fastdfs', 'fastdfs'), (b'nginx', 'nginx')]),
            preserve_default=True,
        ),
    ]
