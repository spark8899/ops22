#!/root/ops/venv/bin/python
# -*- coding: utf-8 -*-
#
#hostname,idc_name,mip,service_type,

import os, sys

proj_path = "/root/ops"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ops.settings")
sys.path.append(proj_path)

os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from cmdb.models import *
import json, time, threading, argparse
#from IPy import IP

host_list = [ host.name for host in Host.objects.all() ]
idc = IDC.objects.all()

#idc = IDC.objects.filter(name="SHW1")
#ss = Host.objects.create(idc=idc[0], name="bb", service_type="ngin") 
#
#ss = Host(idc=idc[0], name="aa", service_type="nginx" )
#ss.save()

print host_list
