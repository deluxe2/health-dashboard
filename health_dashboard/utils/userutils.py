from fastapi import Request


async def verify_user(request: Request) -> str | None:
    return request.session.get("user")
