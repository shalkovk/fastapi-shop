from sqlalchemy.orm import Session
from typing import List
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductListResponse, ProductCreate, ProductResponse
from fastapi import HTTPException, status


class CartSerice:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)
