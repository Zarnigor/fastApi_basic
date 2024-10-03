from typing import Optional

import slugify
from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    name: str = Field(nullable=False, max_length=255)
    products: list["Product"] = Relationship(back_populates="category")

    def __str__(self) -> str:
        return self.name

    @property
    def product_count(self) -> int:
        return len(self.products)




class Product(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    price: int = Field()
    category_id: int = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="products")
    slug: str = Field(default=None, index=True)

    @staticmethod
    def generate_slug(name: str):
        return slugify.slugify(name)

    @classmethod
    def create(cls, name: str, price: int, category_id: int, image_url: str):
        slug = cls.generate_slug(name)
        product = cls(name=name, slug=slug, price=price, category_id=category_id, image_url=image_url)
        return product