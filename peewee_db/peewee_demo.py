python peeweeģ��ʹ��
����и�ETLȡ����Ŀ�� �洢��ʹ�����ݿ⣬ ��Ҫʱ��Ҫ���ж��߳�ת���� ��mysql ���̶߳���̶�д��Ҫע��ĵط�̫�࣬ ���̵߳����ַǳ��鷳��
����ѡ��python orm��
python ��ormģ��ǳ�֮�࣬ ��ȱ��Ҳ�����ԣ� �й��ܱȽ�ȫ���sqlalchemy�� Ҳ��django framework�ṩ��ORM�� ��֮ÿ�����ŵ㣬 ��Ҳ����ȱ�㡣 
��sqlalchemy���ܶ࣬ ���ѧϰ���߾ͳ��ˡ� django framework�ṩ��models������ �кܶ�django���ԣ� ����Щ����Ҳ�ܴ���ȱ�㡣
������һƪ����ר�Ž���python �ڶ�ORM��ѡ��,
SQLAlchemy �������� ORM ���
��ƪ���ͣ� �о�����peewee�� ����������һ��ORMģ�飬 ���Ҳ������ݷǳ�֮�򵥡�


�������ݿ������ģ��
:::shell
python -m pwiz -e mysql -H localhost -p3306 -uroot -Pkkd93kd  web_db > db.py

ģ������
:::python
from peewee import *

database = MySQLDatabase('web_db', **{'host': 'localhost', 'password': 'kkd93kd  ', 'port': 3306, 'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class SyShieldOrder(BaseModel):
    _id = PrimaryKeyField()
    order_up_day = IntegerField(null=True)
    order_up_hours = IntegerField(null=True)
    order_up_moon = IntegerField(null=True)
    order_up_quarter = IntegerField(null=True)
    order_up_week = IntegerField(null=True)
    order_up_year = IntegerField(null=True)
    tu_shopid = CharField(null=True)

    class Meta:
        db_table = 'sy_shield_order'

class SyShieldUser(BaseModel):
    _id = PrimaryKeyField()
    tu_account = CharField(null=True)
    tu_area = CharField(null=True)
    tu_city = CharField(null=True)
    tu_commence = DateField(null=True)
    tu_contract = DateField(null=True)
    tu_cost = IntegerField(null=True)
    tu_domain = CharField(null=True)
    tu_nick = CharField(null=True)
    tu_platform = CharField(null=True)
    tu_province = CharField(null=True)
    tu_realcost = IntegerField(null=True)
    tu_shopid = CharField(null=True)
    tu_version = CharField(null=True)

    class Meta:
        db_table = 'sy_shield_user'

����
:::python

from datetime import datetime
from src import *

database.connect()

for i in SyShieldUser.select():
    print i.tu_account
    print i.__dict__

for i in range(10):
    data = {
            'tu_account': "user_%s" % str(i),
            'tu_area': "HuaDong",
            'tu_city': "Shanghai",
            }
    print SyShildUser.create(tu_account="user", tu_area="HuaDong", tu_city="Shanghai"