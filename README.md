# ops
web ops system

Quick start
===========

> You need a mysql instance running locally or remotely to connect. 
> ops runs on Python 2.7
> install virtualenv pip python-dev

0. install pip

```bash
download https://pypi.python.org/pypi/pip#downloads
# tar zxvf pip-*.tar.gz && cd pip*
# python setup.py install  #required python-setuptools
# vi ~/.pip/pip.conf
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

1. Get ops

```bash
# git clone https://github.com/spark8103/ops.git
# cd ops
# virtualenv venv
# ./venv/bin/pip install -r requirements.txt
```

2. setting Mysql 

```bash
mysql> create database ops;
mysql> grant all on ops.table to ops@localhost;
mysql> set password for ops@localhost = password('xxxxx');
mysql> flush privileges;

# cat ops/settings.py
```

3. Run

```bash
# ./venv/bin/python manage.py migrate
# ./venv/bin/python manage.py runserver 0.0.0.0:80
```

## License
This project is licensed under the [MIT license](https://opensource.org/licenses/MIT).
