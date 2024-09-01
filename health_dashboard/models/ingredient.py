from beanie import Document


class Ingredient(Document):
    name: str
    calories: int
    carbs: int
    sugars: int
    proteins: int
    fats: int
    saturated_fats: int
    barcode: int
    image: str
