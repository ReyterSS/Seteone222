# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
#
# from sqlalchemy.orm import sessionmaker
# # from Postgresql.Postgresql.models import Items, create_items_table, db_connect
# from .spiders.S import db_connect, create_items_table
#
# class SeteonePipeline:
#     def __init__(self):
#         """
#         Initializes database connection and sessionmaker.
#         Creates items table.
#         """
#
#         engine = db_connect()
#         create_items_table(engine)
#         self.Session = sessionmaker(bind=engine)
#
#     def process_item(self, item, spider):
#         """
#         Process the item and store to database.
#         """
#         session = self.Session()
#         instance = session.query(Items).filter_by(**item).one_or_none()
#         if instance:
#             return instance
#         zelda_item = Items(**item)
#         try:
#             session.add(zelda_item)
#             session.commit()
#         except:
#             session.rollback()
#             raise
#         finally:
#             session.close()
#         return item