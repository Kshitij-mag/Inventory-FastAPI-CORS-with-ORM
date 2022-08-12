from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    quantity_in_stock: int
    quantity_sold: int
    unit_price: float
    supplied_by: int
    # class Config:
    #     orm_mode = True


class ProductOut(ProductIn):
    id: int
    revenue: float


class SupplierIn(BaseModel):
    name: str
    company: str
    email: str
    phone: str


class SupplierOut(SupplierIn):
    id: int

    class Config:
        orm_mode = True
