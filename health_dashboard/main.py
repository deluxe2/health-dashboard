from fastapi import FastAPI

from starlette.middleware.sessions import SessionMiddleware
from health_dashboard.database import db

from health_dashboard.dependencies import VerifyDependency
from health_dashboard.settings import settings

import health_dashboard.controllers.authcontroller


app = FastAPI(lifespan=db)
app.add_middleware(SessionMiddleware, secret_key=settings.session_secret)

app.include_router(health_dashboard.controllers.authcontroller.router)


@app.get("/")
async def read_root(user: VerifyDependency):
    if not user:
        return {"message": "Hello World"}
    return {"message": f"Hello {user}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
