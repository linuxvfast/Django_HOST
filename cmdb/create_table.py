import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.10.22/code",encoding='utf-8',echo=True)
base = declarative_base()

class Userinfo(base):
    __tablename__ = 'user_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user = Column(String(32))
    pwd = Column(String(64))

    __table_args__ = {
        'mysql_charset': 'utf8',
        'mysql_engine': 'InnoDB'
    }


class Hostinfo(base):
    __tablename__ = 'host_info'
    id = Column(Integer,primary_key=True,autoincrement=True)
    ip = Column(String(15))
    login_port = Column(Integer,default=22)
    server = Column(String(32))
    login_user = Column(String(32),default='root')
    listen_port = Column(Integer)
    login_pwd = Column(String(64))

    __table_args__ = {
        'mysql_charset': 'utf8',
        'mysql_engine': 'InnoDB'
    }

base.metadata.create_all(engine)

session_class = sessionmaker(bind=engine)
session = session_class()

# user1 = Userinfo(user='root',pwd='root123')
# user2 = Userinfo(user='test',pwd='test123')
# user3 = Userinfo(user='tom',pwd='tom123')
# user4 = Userinfo(user='sicre',pwd='sicre123')
#
# host1 = Hostinfo(ip='192.168.10.22',login_port=22,server='mysqld',login_user='root',listen_port=3306,login_pwd='123456')
# host2 = Hostinfo(ip='192.168.10.50',login_port=22,server='nginx',login_user='root',listen_port=80,login_pwd='123456')
# host3 = Hostinfo(ip='192.168.10.71',login_port=22,server='mongod',login_user='root',listen_port=27017,login_pwd='123456')
#
#
# session.add_all([user1,user2,user3,user4,host1,host2,host3])
# session.commit()
# session.close()