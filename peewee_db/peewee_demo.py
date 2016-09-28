python peewee模块使用
最近有个ETL取数项目， 存储端使用数据库， 必要时候还要进行多线程转换， 而mysql 多线程多进程读写需要注意的地方太多， 多线程调试又非常麻烦。
所有选择python orm。
python 中orm模块非常之多， 优缺点也很明显， 有功能比较全面的sqlalchemy， 也有django framework提供的ORM。 总之每个都优点， 但也单来缺点。 
如sqlalchemy功能多， 相对学习曲线就长了。 django framework提供的models操作， 有很多django特性， 但这些特性也能带来缺点。
这里有一篇博客专门讲了python 众多ORM的选择,
SQLAlchemy 和其他的 ORM 框架
本篇博客， 研究的是peewee。 超级轻量的一个ORM模块， 而且操作数据非常之简单。


根据数据库表生成模型
:::shell
python -m pwiz -e mysql -H localhost -p3306 -uroot -Pkkd93kd  web_db > db.py

模型样例
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

操作
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