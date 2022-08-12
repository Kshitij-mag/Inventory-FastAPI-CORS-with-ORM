from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity_in_stock = Column(Integer, default=0)
    quantity_sold = Column(Integer, default=0)
    unit_price = Column(Float, default=0.00)
    revenue = Column(Float, default=0.00)
    supplied_by = Column(Integer, ForeignKey('suppliers.id'))

    supplier = relationship("Supplier", back_populates="product")


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company = Column(String)
    email = Column(String)
    phone = Column(String)

    product = relationship("Product", back_populates="supplier")

    # images = relationship("Image", back_populates="uploader")

    # uploader = relationship("User", back_populates="images")
