from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

from health_dashboard.dependencies import OAuthDependency, UserDependency


router = APIRouter(tags=["auth"])


@router.get("/login")
async def login(request: Request, auth: OAuthDependency):
    if not auth:
        raise HTTPException(status_code=500, detail="OAuth not configured")
    redirect_uri = request.url_for("auth_callback")
    return await auth.external.authorize_redirect(request, redirect_uri)


@router.get("/auth_callback")
async def auth_callback(
    request: Request, auth: OAuthDependency, userrepo: UserDependency
):
    if not auth:
        raise HTTPException(status_code=500, detail="OAuth not configured")
    response = await auth.external.authorize_access_token(request)
    user = await userrepo.get_or_create(response["userinfo"])
    request.session["user"] = user.name
    return RedirectResponse(url="/")

@router.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")
