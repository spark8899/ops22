# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deploy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u9879\u76ee\u540d\u79f0', choices=[(b'acc', 'eif-acc-web'), (b'aci', 'eif-accing-web'), (b'cas', 'eif-cashier-web'), (b'cms', 'eif-cms'), (b'contract', 'eif-contract-web'), (b'cweb', 'eif-customer-website'), (b'fds', 'eif-fds-web'), (b'fdsb', 'eif-fds-bridge-web'), (b'fdsjob', 'eif-fds-job'), (b'fis', 'eif-fis-web'), (b'fisjob', 'eif-fis-job'), (b'ftc', 'eif-ftc-web'), (b'ftcjob', 'eif-ftc-job'), (b'gotong', 'eif-gotong-web'), (b'mkt', 'eif-market-web'), (b'mktweb', 'eif-market-website'), (b'mbr', 'eif-member-web'), (b'mob', 'eif-mobile-website'), (b'mtp', 'eif-mtp-web'), (b'ofc', 'eif-ofc-web'), (b'omc', 'eif-omc-web'), (b'pc', 'eif-paycore-web'), (b'pcf', 'eif-paycore-frontedge-web'), (b'pcjob', 'eif-paycore-job'), (b'risk', 'eif-risk-web'), (b'setting', 'eif-setting-web'), (b'transcore', 'eif-transcore-web'), (b'vat', 'eif-verify-accounting-web')])),
                ('deploy_time', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('version', models.CharField(max_length=50, verbose_name='git version')),
                ('description', models.TextField(null=True, verbose_name='desc', blank=True)),
                ('db', models.TextField(default=b'\xe5\x90\xa6', blank=True)),
                ('disconf', models.TextField(default=b'\xe5\x90\xa6', blank=True)),
                ('lts', models.TextField(default=b'\xe5\x90\xa6', blank=True)),
                ('mq', models.TextField(default=b'\xe5\x90\xa6', blank=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u4e0a\u7ebf\u53d1\u5e03',
                'verbose_name_plural': '\u4e0a\u7ebf\u53d1\u5e03',
            },
            bases=(models.Model,),
        ),
    ]
