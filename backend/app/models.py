from sqlalchemy import URL, create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base


url_sqllite = URL.create('sqlite', database='database.db')
engine = create_engine(url_sqllite)
Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'user_db'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    admin = Column(Boolean, nullable=False, default=False, server_default='0')


class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)


class InventoryTransaction(Base):
    __tablename__ = 'inventory_transaction'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_type = Column(String)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)
    transaction_date = Column(Integer)
    transaction_value = Column(Float)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('category.category_id'))
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id'))
    stock_level = Column(Integer)


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False)
    description = Column(String)


class ProductImage(Base):
    __tablename__ = 'product_image'

    image_id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    image_alt_text = Column(String)
    image_order = Column(Integer)
    for_thumbnail = Column(Boolean, nullable=False, default=False, server_default='0')


class Supplier(Base):
    __tablename__ = 'supplier'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)


Base.metadata.create_all(engine)