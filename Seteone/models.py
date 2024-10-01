from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
# from Seteone.Seteone import settings
# from Postgresql.Postgresql import settings

Base = declarative_base()

# def db_connect():
#     username = 'avnadmin'
#     password = 'AVNS_OZaFMf--rCU9QzzfxpE'
#     host = 'mysql-198e88e7-sszapis-39be.g.aivencloud.com'
#     port = '22057'  # Порт по умолчанию для MySQL
#     database = 'defaultdb'
#     DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"  # # "mysql+mysqldb://{username}:{password}@{hostname}/{databasename}" mysqldb
#     # engine = create_engine(DATABASE_URL)
#     return create_engine(DATABASE_URL, echo=True)
    # return create_engine(URL(**settings.DATABASE))
#


# class Character(Base):
#     __tablename__ = 'products'
#     Shop_Number = Column(Integer, primary_key=True)
#     Title = Column(String(255))
#     Date = Column(String(255))
#     _40202_5G = Column(String(255))
    # __tablename__ = "Items"
    # name = Column("name", String, primary_key=True)
    # price = Column("price", Integer)

# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
# from .spiders.S import  Base
#
# # Base = declarative_base()
#
#
# class Character(Base):
#     __tablename__ = 'products'
#     Shop_Number = Column(Integer, primary_key=True)
#     Title = Column(String(255))
#     Date = Column(String(255))
#     _40202_5G = Column(String(255))
    # _402030G = Column(String(255))
    # _30102_5G = Column(String(255))
    # _30132_5G = Column(String(255))
    # _50102_5G = Column(String(255))
    # _301232OZC = Column(String(255))
    # _50101G = Column(String(255))
    # _301032OZ = Column(String(255))
    # _402032OZRTUN = Column(String(255))
    # _30932OZ = Column(String(255))
    # _10750444 = Column(String(255))
    # _3092_5G = Column(String(255))
    # _3081G = Column(String(255))
    # _301330G = Column(String(255))
    # _3012250GC = Column(String(255))
    # _108SS = Column(String(255))
    # _30832OZ = Column(String(255))
    # _30732OZ_NLA = Column(String(255))
    # _301332OZ = Column(String(255))
    # _30830G = Column(String(255))
    # _30130G = Column(String(255))
    # _308250G = Column(String(255))
    # _501030G = Column(String(255))
    # _101B = Column(String(255))
    # _1017PEACH = Column(String(255))
    # _501055G = Column(String(255))
    # _10140CA = Column(String(255))
    # _10140 = Column(String(255))
    # _10940CPG = Column(String(255))
    # _109SSCPG = Column(String(255))