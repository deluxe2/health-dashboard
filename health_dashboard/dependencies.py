from functools import lru_cache
from typing import Annotated
from fastapi import Depends

from authlib.integrations.starlette_client import OAuth

from health_dashboard.utils.userutils import verify_user

from health_dashboard.settings import Settings
from health_dashboard.repositories.mealrepository import MealRepository
from health_dashboard.repositories.userrepository import UserRepository
from health_dashboard.repositories.weightrepository import WeightRepository


@lru_cache
def getsettings():
    return Settings()


ConfigDependency = Annotated[Settings, Depends(getsettings)]


@lru_cache
def oauth(conf: ConfigDependency) -> OAuth | None:
    if not all([conf.client_id, conf.client_secret, conf.server_metadata_url]):
        return None
    oauth = OAuth()
    oauth.register(
        "external",
        client_id=conf.client_id,
        client_secret=conf.client_secret,
        server_metadata_url=conf.server_metadata_url,
        client_kwargs={"scope": f"openid profile email {conf.group_scope}"},
    )
    return oauth


OAuthDependency = Annotated[OAuth | None, Depends(oauth)]
VerifyDependency = Annotated[str | None, Depends(verify_user)]


UserDependency = Annotated[UserRepository, Depends(UserRepository)]
MealDependency = Annotated[MealRepository, Depends(MealRepository)]
WeightDependency = Annotated[WeightRepository, Depends(WeightRepository)]
