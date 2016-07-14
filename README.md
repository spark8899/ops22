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
yum install mysql mysql-devel
docker run -d --restart=always --name mysql -v /home/mysql:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e TZ="Asia/Shanghai" mysql:5.6.30

mysql -uroot -p123456 -h localhost
mysql> CREATE DATABASE IF NOT EXISTS ops COLLATE utf8_general_ci;  
mysql> GRANT all privileges on ops.* to ops@'%' identified by '123456';
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
