from typing import List
from beanie import Document
from pymongo.results import DeleteResult


class BaseRepository[T: Document]:
    async def get(self, id: str) -> T | None:
        return await T.get(id)

    async def get_all(self, skip: int = 0, limit: int = 25) -> List[T]:
        return await T.find().skip(skip), limit(limit).to_list()

    async def create(self, obj: T) -> T:
        return await obj.insert()

    async def update(self, obj: T) -> T:
        await obj.replace()
        return obj

    async def update_many(self, objs: List[T]) -> List[T]:
        await T.replace_many(objs)
        return objs

    async def delete(self, obj: T) -> DeleteResult | None:
        return await obj.delete()
