from health_dashboard.models.user import User
from health_dashboard.repositories.baserepository import BaseRepository


class UserRepository(BaseRepository[User]):
    async def get_or_create(self, userinfo: dict[str, str]) -> User:
        user = await User.find(User.name == userinfo["name"]).first_or_none()
        if user:
            return user
        user = User(name=userinfo["name"], email=userinfo["email"])
        await user.save()
        return user
