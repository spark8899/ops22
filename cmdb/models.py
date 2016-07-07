# -*- coding: utf-8 -*-
from django.db import models

SERVER_STATUS = (
    (0, u"Normal"),
    (1, u"Down"),
    (2, u"No Connect"),
    (3, u"Error"),
)
SERVICE_TYPES = (
    ('app', u"app"),
    ('job', u"job"),
    ('mysql', u"mysql"),
    ('codis', u"codis"),
    ('zookeeper', u"zookeeper"),
    ('dubbo', u"dubbo"),
    ('lts', u"lts"),
    ('rocketmq', u"rocketmq"),
    ('elk', u"elk"),
    ('cat', u"cat"),
    ('fastdfs', u"fastdfs"),
    ('nginx', u"nginx"),
)


class IDC(models.Model):
    name = models.CharField(u"IDC编码", max_length=64)
    address = models.CharField(u"地址", max_length=128)

    contact = models.CharField(u"联系人", max_length=32, blank=True, null=True)
    telphone = models.CharField(u"电话", max_length=32, blank=True, null=True)
    qq = models.CharField(u"QQ", max_length=32, blank=True, null=True)
    customer_id = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(u"备注", blank=True, null=True)

    create_time = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC"
        verbose_name_plural = verbose_name


class Host(models.Model):
    idc = models.ForeignKey(IDC)
    name = models.CharField(u"主机名", max_length=64)
    mip = models.GenericIPAddressField(blank=True, null=True, help_text="manager IP")
    bip = models.GenericIPAddressField(blank=True, null=True, help_text="business IP")
    vip = models.GenericIPAddressField(blank=True, null=True)
    status = models.SmallIntegerField(u"状态", choices=SERVER_STATUS, default=0)

    core_num = models.SmallIntegerField(choices=[(i * 2, "%s Cores" % (i * 2)) for i in range(1, 19)], default=2)
    hard_disk = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)

    system = models.CharField(u"System OS", max_length=32, choices=[(i, i) for i in (u"centOS7.2", u"rh6.5", u"windows")], default="centOS7.2")

    create_time = models.DateField(auto_now=True)
    service_type = models.CharField(max_length=32, choices=SERVICE_TYPES)
    description = models.TextField(u"备注", blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Host"
        verbose_name_plural = verbose_name


class MaintainLog(models.Model):
    host = models.ForeignKey(Host)
    maintain_type = models.CharField(max_length=32)
    time = models.DateTimeField()
    operator = models.CharField(max_length=16)
    note = models.TextField()

    def __unicode__(self):
        return '%s maintain-log [%s] %s %s' % (self.host.name, self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                               self.maintain_type)

    class Meta:
        verbose_name = u"维修日志"
        verbose_name_plural = verbose_name


class HostGroup(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    hosts = models.ManyToManyField(
        Host, verbose_name=u'Hosts', blank=True, related_name='groups')

    class Meta:
        verbose_name = u"Host Group"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class AccessRecord(models.Model):
    date = models.DateField()
    user_count = models.IntegerField()
    view_count = models.IntegerField()

    class Meta:
        verbose_name = u"Access Record"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s Access Record" % self.date.strftime('%Y-%m-%d')
