from sqlalchemy.orm import Session
from typing import List
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductListResponse, ProductCreate, ProductResponse
from fastapi import HTTPException, status


class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all_products(self) -> ProductListResponse:
        products = self.product_repository.get_all()
        product_reponse = [ProductResponse.model_validate(
            product) for product in products]
        return ProductListResponse(products=product_reponse, total=len(product_reponse))
