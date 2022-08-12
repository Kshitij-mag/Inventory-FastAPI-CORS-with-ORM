from curses import def_shell_mode
from math import prod
from fastapi import FastAPI, Depends
from . import models, schemas
from .database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)


@app.get('/')
def index():
    return {"details": "API"}

# Supplier


@app.post('/supplier')
async def add_supplier(supplier_info: schemas.SupplierIn,
                       db: Session = Depends(get_db)):
    supplier = models.Supplier(
        name=supplier_info.name,
        company=supplier_info.company,
        email=supplier_info.email,
        phone=supplier_info.phone
    )
    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier


@app.get('/supplier')
async def get_all_suppliers(db: Session = Depends(get_db)):
    suppliers = db.query(models.Supplier).all()
    return suppliers


@app.get('/supplier/{id}')
async def get_supplier(id: int, db: Session = Depends(get_db)):
    supplier = db.query(models.Supplier).filter(
        models.Supplier.id == id
    ).first()

    return supplier


@app.put('/supplier/{sup_id}')
async def update_supplier(sup_id: int, update_info: schemas.SupplierIn, db: Session = Depends(get_db)):
    supplier = db.query(models.Supplier).filter(
        models.Supplier.id == sup_id
    ).first()

    supplier.name = update_info.name
    supplier.company = update_info.company
    supplier.phone = update_info.phone
    supplier.email = update_info.email
    db.commit()


@app.delete('/supplier/{id}')
async def del_supplier(id: int, db: Session = Depends(get_db)):
    db.query(models.Supplier).filter(
        models.Supplier.id == id
    ).delete()
    db.commit()
    return {"details": "deleted"}


# Product
@app.post('/product')
async def add_product(request: schemas.ProductIn,
                      db: Session = Depends(get_db)):
    product = models.Product(
        name=request.name,
        quantity_in_stock=request.quantity_in_stock,
        quantity_sold=request.quantity_sold,
        unit_price=request.unit_price,
        revenue=request.quantity_sold * request.unit_price,
        supplied_by=request.supplied_by
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@app.get('/product')
async def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@app.get('/product/{id}')
async def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()
    return product


@app.put('/product/{id}')
async def update_product(id: int, request: schemas.ProductIn, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()

    product.name = request.name
    product.quantity_in_stock = request.quantity_in_stock
    product.quantity_sold = request.quantity_sold
    product.unit_price = request.unit_price
    product.supplied_by = request.supplied_by

    db.commit()


@app.delete('/product/{id}')
async def del_product(id: int, db: Session = Depends(get_db)):
    db.query(models.Product).filter(
        models.Product.id == id
    ).delete()
    return {"details": "deleted"}
