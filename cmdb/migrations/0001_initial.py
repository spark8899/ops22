# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('user_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Access Record',
                'verbose_name_plural': 'Access Record',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u4e3b\u673a\u540d')),
                ('mip', models.GenericIPAddressField(help_text=b'manager IP', null=True, blank=True)),
                ('bip', models.GenericIPAddressField(help_text=b'business IP', null=True, blank=True)),
                ('vip', models.GenericIPAddressField(null=True, blank=True)),
                ('status', models.SmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, 'Normal'), (1, 'Down'), (2, 'No Connect'), (3, 'Error')])),
                ('core_num', models.SmallIntegerField(choices=[(2, b'2 Cores'), (4, b'4 Cores'), (6, b'6 Cores'), (8, b'8 Cores'), (10, b'10 Cores'), (12, b'12 Cores'), (14, b'14 Cores'), (16, b'16 Cores'), (18, b'18 Cores'), (20, b'20 Cores'), (22, b'22 Cores'), (24, b'24 Cores'), (26, b'26 Cores'), (28, b'28 Cores'), (30, b'30 Cores'), (32, b'32 Cores'), (34, b'34 Cores'), (36, b'36 Cores')])),
                ('hard_disk', models.IntegerField(null=True, blank=True)),
                ('memory', models.IntegerField(null=True, blank=True)),
                ('system', models.CharField(default=b'centOS7.2', max_length=32, verbose_name='System OS', choices=[('centOS7.2', 'centOS7.2'), ('rh6.5', 'rh6.5'), ('windows', 'windows')])),
                ('create_time', models.DateField(auto_now=True)),
                ('service_type', models.CharField(max_length=32, choices=[(b'nginx', 'Nginx'), (b'tomcat', 'Tomcat'), (b'mysql', 'mysql'), (b'logstash', 'logstash'), (b'app', 'app'), (b'zookeeper', 'zookeeper'), (b'fastdfs', 'fastdfs')])),
                ('description', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Host',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
                ('hosts', models.ManyToManyField(related_name='groups', verbose_name='Hosts', to='cmdb.Host', blank=True)),
            ],
            options={
                'verbose_name': 'Host Group',
                'verbose_name_plural': 'Host Group',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='IDC\u7f16\u7801')),
                ('address', models.CharField(max_length=128, verbose_name='\u5730\u5740')),
                ('contact', models.CharField(max_length=32, null=True, verbose_name='\u8054\u7cfb\u4eba', blank=True)),
                ('telphone', models.CharField(max_length=32, null=True, verbose_name='\u7535\u8bdd', blank=True)),
                ('qq', models.CharField(max_length=32, null=True, verbose_name='QQ', blank=True)),
                ('customer_id', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'IDC',
                'verbose_name_plural': 'IDC',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaintainLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maintain_type', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
                ('operator', models.CharField(max_length=16)),
                ('note', models.TextField()),
                ('host', models.ForeignKey(to='cmdb.Host')),
            ],
            options={
                'verbose_name': '\u7ef4\u4fee\u65e5\u5fd7',
                'verbose_name_plural': '\u7ef4\u4fee\u65e5\u5fd7',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(to='cmdb.IDC'),
            preserve_default=True,
        ),
    ]
