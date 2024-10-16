from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum, Index
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash
import enum
import datetime

Base = declarative_base()

# Enum for customer type and transaction item type
class CustomerType(enum.Enum):
    seller = "seller"
    buyer = "buyer"

class TransactionItemType(enum.Enum):
    achat = "achat"  # purchase
    vent = "vent"    # sale

class PasswordType(enum.Enum):
    admin = "admin"
    user = "user"

# User class with password hashing
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    _password = Column("password", String, nullable=False)
    type = Column(Enum(PasswordType), nullable=False)

    @hybrid_property
    def password(self):
        raise AttributeError("Password is not accessible")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self._password, password)
    

# Customer class
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(String(10), primary_key=True)
    nom = Column(String, nullable=False)
    type = Column(Enum(CustomerType), nullable=False)
    sold = Column(Float, default=0.0)
    
    transactions = relationship("Transaction", back_populates="customer")
    def tolist(self):
        return[self.id,str(self.nom),str(self.type),str(self.sold)]

# Product class
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    qt = Column(Integer, nullable=False)  # Quantity
    pritdachat=Column(Integer, nullable=False)

    categorie_id = Column(Integer, ForeignKey("categories.id"))
    categorie = relationship("Categorie", back_populates="products")

    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("Brand", back_populates="products")

    transaction_items = relationship("TransactionItem", back_populates="product")

# Transaction class
class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.timezone.utc, index=True)
    total = Column(Float, nullable=False)
    versement = Column(Float, nullable=False)  # Payment made
    ensiansold = Column(Float)  # Customer's balance before the transaction
    
    customer_id = Column(String(10), ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="transactions")
    
    transaction_items = relationship("TransactionItem", back_populates="transaction")

# TransactionItem class
class TransactionItem(Base):
    __tablename__ = 'transaction_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(TransactionItemType), nullable=False)
    qt = Column(Float, nullable=False)  # Quantity
    priceachat = Column(Float, nullable=False)  # Purchase price
    price = Column(Float, nullable=False)  # Sale price
    
    transaction_id = Column(Integer, ForeignKey('transactions.id'),index=True)
    transaction = relationship("Transaction", back_populates="transaction_items")
    
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="transaction_items")
    def total(self):
        return self.qt*self.price

# Categorie class
class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)

    products = relationship("Product", back_populates="categorie")

# Brand class
class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)

    products = relationship("Product", back_populates="brand")
