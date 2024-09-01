from datetime import datetime
from typing import List
from beanie import Document, Link
from pydantic import BaseModel

from health_dashboard.models.ingredient import Ingredient
from health_dashboard.models.user import User


class MealIngredient(BaseModel):
    ingredient: Link[Ingredient]
    quantity: int


class Meal(Document):
    name: str
    calories: int
    date: datetime
    description: str
    ingredients: List[MealIngredient]
    image: str
    user: Link[User]
